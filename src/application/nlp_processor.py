from typing import List

import nltk
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')


class NLPProcessor:

    def remove_stop_words(self, text: str) -> str:
        words = self.tokenize_text(text)
        tokens_without_sw = [word for word in words if word.lower() not in stopwords.words()]
        filtered_sentence = " ".join(tokens_without_sw)
        return filtered_sentence

    def tokenize_text(self, text: str) -> List:
        return word_tokenize(text)

    def tokenize_words(self, text: str) -> List:
        tokenizer = RegexpTokenizer(r'\w+')
        return tokenizer.tokenize(text)
