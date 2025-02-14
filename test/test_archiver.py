import unittest
import os
import time
import shutil
import tarfile
import subprocess
import test.conftest
from archiver import (
    check_folder,
    count_files,
    create_files,
    archive_files,
    TMP_FOLDER,
    MAX_ARCHIVE_FILES,
    ARCHIVE_NAME,
)


class TestArchiver(unittest.TestCase):

    def setUp(self):
        check_folder()
        self.cleanup_tmp()

    def tearDown(self):
        self.cleanup_tmp()

    def cleanup_tmp(self):
        if os.path.exists(TMP_FOLDER):
            shutil.rmtree(TMP_FOLDER)
        os.makedirs(TMP_FOLDER)

    def test_check_folder(self):
        shutil.rmtree(TMP_FOLDER, ignore_errors=True)
        check_folder()
        self.assertTrue(os.path.exists(TMP_FOLDER))

    def test_create_files(self):
        create_files()
        self.assertEqual(count_files(), 10)

    def test_archive_files(self):
        create_files()
        archive_files()
        self.assertFalse(os.listdir(TMP_FOLDER))
        self.assertTrue(os.path.exists("files.tar.gz"))

    def test_monitor_folder_run(self):
        result = subprocess.run(
            ["python3", "src/archiver.py", "true"], capture_output=True, text=True
        )
        self.assertIn("files collected", result.stdout)
        self.assertTrue(os.path.exists("files.tar.gz"))
        with tarfile.open(ARCHIVE_NAME, "r:gz") as tar:
            self.assertEqual(len(tar.getnames()), MAX_ARCHIVE_FILES)

    def test_existing_tmp_folder_with_more_than_10_files(self):
        check_folder()
        for i in range(15):
            with open(os.path.join(TMP_FOLDER, f"test_file_{i}.txt"), "w") as f:
                f.write("Test file content")
        result = subprocess.run(
            ["python3", "src/archiver.py", "true"], capture_output=True, text=True
        )
        self.assertEqual(len(os.listdir(TMP_FOLDER)), 0)
        with tarfile.open("files.tar.gz", "r:gz") as tar:
            self.assertEqual(len(tar.getnames()), 10)


if __name__ == "__main__":
    unittest.main()
