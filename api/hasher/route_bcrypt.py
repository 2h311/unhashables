from typing import Optional

from fastapi import FastAPI, APIRouter, Body

from api.hasher import Hasher

router = APIRouter()


@router.post("/encrypt")
def encrypt_route(
    string: str = Body(..., embed=True), rounds: Optional[str] = Body(..., embed=True)
):
    hash = Hasher.get_hash(string, rounds)
    return {"hash": hash}


@router.post("/verify")
def verify_route(
    plain_string: str = Body(..., embed=True), hash_string: str = Body(..., embed=True)
):
    result = Hasher.verify_hash(plain_string, hash_string)
    return {"response": "Match!" if result else "Not a match!"}
