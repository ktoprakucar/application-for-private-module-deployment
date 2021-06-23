import os
from typing import AnyStr


class FileReader:

    def read_file(self, file_name: str) -> AnyStr:
        with open(os.path.dirname(os.path.abspath(__file__)) + "/resources/" + file_name,
                  "r",
                  ) as query_file:
            return query_file.read()
