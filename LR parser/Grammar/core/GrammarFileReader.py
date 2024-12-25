from typing import List


class GrammarFileReader:
    def __call__(self, filename: str) -> List[str]:
        raise NotImplementedError
