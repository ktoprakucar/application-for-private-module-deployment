import unittest

from src.application.nlp_processor import NLPProcessor


class NLPProcessorTest(unittest.TestCase):

    def create_text(self):
        return "The hallway smelt of boiled cabbage and old rag mats. " \
               "At one end of it a coloured poster, too large for indoor display, " \
               "had been tacked to the wall. It depicted simply an enormous face, " \
               "more than a metre wide: the face of a man of about forty-five, " \
               "with a heavy black moustache and ruggedly handsome features. " \
               "Winston made for the stairs. It was no use trying the lift. " \
               "Even at the best of times it was seldom working, " \
               "and at present the electric current was cut off during daylight hours. " \
               "It was part of the economy drive in preparation for HateWeek. " \
               "The flat was seven flights up, and Winston, who was thirty-nine and " \
               "had a varicose ulcer above his right ankle, went slowly, " \
               "resting several times on the way. On each landing, " \
               "opposite the lift shaft, the poster with the enormous face gazed from the wall. " \
               "It was one of those pictures which are so contrived that " \
               "the eyes follow you about when you move. BIG BROTHER IS WATCHING YOU, " \
               "the caption beneath it ran."

    def create_pre_removed_text(self):
        return "hallway smelt boiled cabbage old rag mats . coloured poster , " \
               "large indoor display , tacked wall . depicted simply enormous , " \
               "metre wide : forty-five , heavy black moustache ruggedly handsome features . " \
               "Winston made stairs . use trying lift . Even best times seldom working , " \
               "present electric current cut daylight hours . part economy drive preparation HateWeek . " \
               "flat seven flights , Winston , thirty-nine varicose ulcer right ankle , went slowly , " \
               "resting several times way . landing , opposite lift shaft , poster enormous gazed wall . " \
               "pictures contrived eyes follow move . BIG BROTHER WATCHING , caption beneath ran ."

    def create_tokenized_words(self):
        return ['The', 'hallway', 'smelt', 'of', 'boiled', 'cabbage', 'and', 'old', 'rag', 'mats', 'At', 'one', 'end',
                'of', 'it', 'a', 'coloured', 'poster', 'too', 'large', 'for', 'indoor', 'display', 'had', 'been',
                'tacked', 'to', 'the', 'wall', 'It', 'depicted', 'simply', 'an', 'enormous', 'face', 'more', 'than',
                'a', 'metre', 'wide', 'the', 'face', 'of', 'a', 'man', 'of', 'about', 'forty', 'five', 'with', 'a',
                'heavy', 'black', 'moustache', 'and', 'ruggedly', 'handsome', 'features', 'Winston', 'made', 'for',
                'the', 'stairs', 'It', 'was', 'no', 'use', 'trying', 'the', 'lift', 'Even', 'at', 'the', 'best', 'of',
                'times', 'it', 'was', 'seldom', 'working', 'and', 'at', 'present', 'the', 'electric', 'current', 'was',
                'cut', 'off', 'during', 'daylight', 'hours', 'It', 'was', 'part', 'of', 'the', 'economy', 'drive', 'in',
                'preparation', 'for', 'HateWeek', 'The', 'flat', 'was', 'seven', 'flights', 'up', 'and', 'Winston',
                'who', 'was', 'thirty', 'nine', 'and', 'had', 'a', 'varicose', 'ulcer', 'above', 'his', 'right',
                'ankle', 'went', 'slowly', 'resting', 'several', 'times', 'on', 'the', 'way', 'On', 'each', 'landing',
                'opposite', 'the', 'lift', 'shaft', 'the', 'poster', 'with', 'the', 'enormous', 'face', 'gazed', 'from',
                'the', 'wall', 'It', 'was', 'one', 'of', 'those', 'pictures', 'which', 'are', 'so', 'contrived', 'that',
                'the', 'eyes', 'follow', 'you', 'about', 'when', 'you', 'move', 'BIG', 'BROTHER', 'IS', 'WATCHING',
                'YOU', 'the', 'caption', 'beneath', 'it', 'ran']

    def test_should_remove_stop_words(self):
        # given
        text = self.create_text()

        processor = NLPProcessor()

        # when
        removed_text = processor.remove_stop_words(text)

        # then
        pre_removed_text = self.create_pre_removed_text()
        self.assertIsNotNone(removed_text)
        self.assertEqual(removed_text, pre_removed_text)

    def test_should_count_words(self):
        # given
        text = self.create_text()

        processor = NLPProcessor()

        # when
        words = processor.tokenize_words(text)

        # then
        tokenized_words = self.create_tokenized_words()
        self.assertIsNotNone(words)
        self.assertTrue(len(words), 176)
        self.assertEqual(words, tokenized_words)
