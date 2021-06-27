import unittest

from src.application.file_reader import FileReader


class FileReaderTest(unittest.TestCase):

    def test_should_read_the_file(self):
        # given
        file_name = 'snow.txt'

        file_reader = FileReader()

        # when
        text = file_reader.read_file(file_name)

        # then
        self.assertIsNotNone(text)

    def test_should_raise_an_exception_when_text_is_not_found(self):
        # given
        file_name = 'a_moveable_feast.txt'

        file_reader = FileReader()

        # when
        with self.assertRaises(Exception) as context:
            text = file_reader.read_file(file_name)

        # then
        self.assertTrue('No such file or directory' in str(context.exception))
