import unittest

from src.application.language_application import LanguageApplication


class ApplicationIntegrationTest(unittest.TestCase):

    def _pre_cleaned_text(self):
        return "Ka poet , returns Turkey 12 years political exile Germany . several motives , first , journalist , " \
               "investigate suicides hope meeting woman used know . Heavy snow cuts town three days time Ka " \
               "conversation former communist , secularist , fascist nationalist , possible Islamic extremist , " \
               "Islamic moderates , young Kurds , military , Secret Service , police particular , " \
               "actor-revolutionary . midst , love passion found . Temporarily closed world , farcical coup " \
               "staged linked melodramatically stage play . main discussion concerns interface secularism belief " \
               "references Turkey 's twentieth century history ."

    def test_should_clean_stop_words_from_text(self):
        # given
        file_name = 'snow.txt'
        language_application = LanguageApplication()

        # when
        cleaned_text = language_application.clean_stop_words(file_name)

        # then
        pre_cleaned_text = self._pre_cleaned_text()
        self.assertIsNotNone(cleaned_text)
        self.assertEqual(cleaned_text, pre_cleaned_text)

    def test_should_return_word_count(self):
        # given
        file_name = '1984.txt'
        language_application = LanguageApplication()

        # when
        word_count = language_application.count_words(file_name)

        # then
        self.assertIsNotNone(word_count)
        self.assertTrue(word_count, 142)
