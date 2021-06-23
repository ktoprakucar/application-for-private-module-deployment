from src.application.file_reader import FileReader
from src.application.nlp_processor import NLPProcessor


class Application:

    def __init__(self):
        self._nlp_processor = NLPProcessor()
        self._file_reader = FileReader()

    def clean_stop_words(self, file_name: str) -> str:
        text = self._file_reader.read_file(file_name)
        filtered_sentence = self._nlp_processor.remove_stop_words(text)
        return filtered_sentence

    def count_words(self, file_name: str) -> int:
        text = self._file_reader.read_file(file_name)
        words = self._nlp_processor.tokenize_words(text)
        return len(words)
