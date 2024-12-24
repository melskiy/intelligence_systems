from typing import List


class TokenRepository:

    def get_tokens(self) -> List[str]:
        raise NotImplementedError

    def add_token(self, token: str) -> None:
        raise NotImplementedError
