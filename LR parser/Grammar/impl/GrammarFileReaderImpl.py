from typing import List

from Grammar.core import GrammarFileReader


class GrammarFileReaderImpl(GrammarFileReader):
    def __call__(self, filename: str) -> List[str]:
        try:
            with open(filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"Grammar file {filename} not found")
        except Exception as e:
            raise Exception(f"Error reading grammar file: {str(e)}")
