import unittest

import venv_checker

from subprocess import call

class VenvVersionTestCase(unittest.TestCase):
    def test_python27(self):
        expected_version = '2.7'
        path_to_venv = '/tmp/test'
        call('/usr/local/bin/virtualenv -p /usr/bin/python2.7 ' + path_to_venv, shell=True)
        result = venv_checker.get_version(path_to_venv)
        self.assertEquals(result, expected_version)

if __name__ == '__main__':
    unittest.main()

