
import os
import shutil
import subprocess
import tempfile
import unittest

from venv_checker import get_version


class VenvCheckerTest(unittest.TestCase):
    def setUp(self):
        self.virtualenvs = {}

        mk_venv_command = '/usr/local/bin/virtualenv -p {python_path} {path}'
        for ii, version in enumerate(['2.7', '3.3', '3.4']):
            path = tempfile.mkdtemp(dir='/tmp')

            python_path = subprocess.check_output(
                'which python{}'.format(version), shell=True
            ).decode('UTF-8').rstrip('\n')

            subprocess.check_call(
                mk_venv_command.format(path=path, python_path=python_path),
                shell=True
            )
            self.virtualenvs[version] = path

    def tearDown(self):
        for path in self.virtualenvs.values():
            shutil.rmtree(path)

    def test_works_with_python27(self):
        self.assertEqual(get_version(self.virtualenvs['2.7']), '2.7')

    def test_works_with_python33(self):
        self.assertEqual(get_version(self.virtualenvs['3.3']), '3.3')

    def test_works_with_python34(self):
        self.assertEqual(get_version(self.virtualenvs['3.4']), '3.4')

    def test_errors_on_weird_lib_folder(self):
        pass

    def test_errors_on_wrong_venv_path(self):
        pass

