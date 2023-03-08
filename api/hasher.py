from passlib import hash


class Hasher:
    @staticmethod
    def verify_hash(plain_string: str, hashed_string: str) -> bool:
        return hash.bcrypt.verify(plain_string, hashed_string)

    @staticmethod
    def get_hash(plain_string: str, rounds: int | str = 5) -> str:
        return hash.bcrypt.hash(plain_string, rounds=int(rounds))
