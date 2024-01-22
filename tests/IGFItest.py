import unittest
from unittest.mock import patch
import sys

class TestIGFIScript(unittest.TestCase):

    def setUp(self):
        self.original_stdout = sys.stdout

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_valid_input(self):
        with patch('builtins.input', side_effect=['1', '5']):
            with self.assertRaises(SystemExit) as cm:
                import igfi
            self.assertEqual(cm.exception.code, 0)

    def test_invalid_python_version(self):
        with patch('sys.version_info', (2, 7, 10, 'final', 0)):
            with patch('builtins.input', side_effect=['1', '5']):
                with self.assertRaises(SystemExit) as cm:
                    import igfi
                self.assertEqual(cm.exception.code, 0)

    def test_missing_required_packages(self):
        with patch('sys.modules', {'rich': None}):
            with patch('builtins.input', side_effect=['1', '5']):
                with self.assertRaises(SystemExit) as cm:
                    import igfi
                self.assertEqual(cm.exception.code, 0)

    def test_root_user_linux(self):
        with patch('sys.platform', 'linux'):
            with patch('os.geteuid', return_value=0):
                with patch('builtins.input', side_effect=['1', '5']):
                    with self.assertRaises(SystemExit) as cm:
                        import igfi
                    self.assertEqual(cm.exception.code, 0)

    def test_invalid_username_input(self):
        with patch('builtins.input', side_effect=['1', 'ausernamenoonewouldeveruse321', '5']):
            with self.assertRaises(SystemExit) as cm:
                import igfi
            self.assertEqual(cm.exception.code, 0)

    def test_uninstall_option(self):
        with patch('builtins.input', side_effect=['4']):
            with self.assertRaises(SystemExit) as cm:
                import igfi
            self.assertEqual(cm.exception.code, 0)

    def test_info_display(self):
        with patch('builtins.input', side_effect=['2', '5']):
            with self.assertRaises(SystemExit) as cm:
                import igfi
            self.assertEqual(cm.exception.code, 0)

    def test_clear_log(self):
        with patch('os.path.exists', return_value=True):
            with patch('os.remove'):
                with patch('builtins.input', side_effect=['3', '5']):
                    with self.assertRaises(SystemExit) as cm:
                        import igfi
                    self.assertEqual(cm.exception.code, 0)

    def test_session_file_not_found(self):
        with patch('os.path.exists', return_value=False):
            with patch('builtins.input', side_effect=['1', '5']):
                with self.assertRaises(SystemExit) as cm:
                    import igfi
                self.assertEqual(cm.exception.code, 0)

    def test_valid_operation(self):
        with patch('builtins.input', side_effect=['1', 'yes', 'yes', '5']):
            with self.assertRaises(SystemExit) as cm:
                import igfi
            self.assertEqual(cm.exception.code, 0)

if __name__ == '__main__':
    unittest.main()
