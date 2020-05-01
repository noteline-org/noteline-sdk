import unittest
import shutil
import os

from noteline.core import noteline_notebook

ORIGINAL_NOTEBOOK_FILE_NAME="test/noteline/core/test.ipynb"
TEST_NOTEBOOK_FOLDER="/tmp"
TEST_NOTEBOOK_FILE_NAME="{}/test.ipynb".format(TEST_NOTEBOOK_FOLDER)


class TestNotelineNotebook(unittest.TestCase):

    def setUp(self):
        shutil.copy(ORIGINAL_NOTEBOOK_FILE_NAME, TEST_NOTEBOOK_FOLDER)

    def tearDown(self):
        os.remove(TEST_NOTEBOOK_FILE_NAME)

    def test_metadata_set_get(self):
        env_name = "name1"
        env_type = "type1"
        env_uri = "uri1"

        nb = noteline_notebook.get_noteline_notebook(TEST_NOTEBOOK_FILE_NAME)

        nb.set_env(name=env_name, type=env_type, uri=env_uri)
        nb.save_notebook(TEST_NOTEBOOK_FILE_NAME)

        nb = noteline_notebook.get_noteline_notebook(TEST_NOTEBOOK_FILE_NAME)
        env = nb.get_env()
        self.assertEqual(env["name"], env_name)
        self.assertEqual(env["type"], env_type)
        self.assertEqual(env["uri"], env_uri)
