import importlib.util
from io import BytesIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/download.py'
spec = importlib.util.spec_from_file_location('download', SCRIPT)
download = importlib.util.module_from_spec(spec)
spec.loader.exec_module(download)


class Response(BytesIO):
    def __init__(self, data, content_type, length=None):
        super().__init__(data)
        self.headers = {'Content-Type': content_type, 'Content-Length': str(length if length is not None else len(data))}


class DownloadTests(unittest.TestCase):
    def test_html_login_rejected_even_with_image_name(self):
        with self.assertRaisesRegex(ValueError, 'HTML'):
            download.verify_content('frame.jpg', 'text/html', b'<!DOCTYPE html><html>Sign in</html>')

    def test_wrong_archive_header_rejected(self):
        with self.assertRaisesRegex(ValueError, 'ZIP'):
            download.verify_content('day.zip', 'application/octet-stream', b'access denied')

    def test_latest_sensor_version_selected_without_quicklook(self):
        template = 'radflux_1a_Lz2M1minI2apPrayDp_v{:02d}_20210417_000000_1440.txt'
        names = [template.format(6), template.format(7), 'radiation.png', 'other_sensor_v99.txt']
        self.assertEqual(download.latest_radiation_file(names), template.format(7))

    def test_query_file_uses_jpeg_filename(self):
        self.assertEqual(download.safe_filename('https://example.com/download.php?file=A/B/frame.jpg'), 'frame.jpg')
        with self.assertRaises(ValueError):
            download.safe_filename('https://example.com/download.php?file=..')

    def test_truncated_transfer_cleans_partial(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            with patch.object(download, 'open_url', return_value=Response(b'\xff\xd8\xfftest', 'image/jpeg', length=100)):
                with self.assertRaisesRegex(ValueError, '不完整'):
                    download.fetch_file('https://example.com/frame.jpg', folder)
            self.assertEqual(list(folder.iterdir()), [])

    def test_existing_file_and_existing_partial_are_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            existing = folder / 'frame.jpg'
            existing.write_bytes(b'old')
            with self.assertRaisesRegex(ValueError, '已存在'):
                download.fetch_file('https://example.com/frame.jpg', folder)
            self.assertEqual(existing.read_bytes(), b'old')
            existing.unlink()
            partial = folder / 'frame.jpg.part'
            partial.write_bytes(b'previous attempt')
            with self.assertRaisesRegex(ValueError, '未完成'):
                download.fetch_file('https://example.com/frame.jpg', folder)
            self.assertEqual(partial.read_bytes(), b'previous attempt')

    def test_success_saves_content_without_partial(self):
        data = b'\xff\xd8\xfftest'
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            with patch.object(download, 'open_url', return_value=Response(data, 'image/jpeg')):
                path, size = download.fetch_file('https://example.com/frame.jpg', folder)
            self.assertEqual(path.read_bytes(), data)
            self.assertEqual(size, len(data))
            self.assertFalse((folder / 'frame.jpg.part').exists())

    def test_remote_catalogue_cannot_redirect_download_to_another_host(self):
        site = next(s for s in download.CATALOG['sites'] if s['id'] == 'copdd')
        with patch.object(download, 'read_listing', return_value='{"urls":["https://other.example/frame.jpg"]}'):
            with self.assertRaisesRegex(ValueError, '非预期'):
                download.resolve(site, download.date(2021, 4, 17), None, 'images')


if __name__ == '__main__':
    unittest.main()
