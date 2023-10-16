from fastapi import FastAPI
from typing import Union
from schema import Pet, PetResponse
from uuid import UUID
app = FastAPI()


@app.post("/pet", status_code=201)
def post_pet(pet: Pet):
    pass

@app.post("/pet")
def post_pet(pet: Pet) -> PetResponse:
    pass

@app.get("/pet")
def get_pets(
    skip: int = 0,
    limit: int = 10,
    order: str | None = None
) -> list[Pet]:
    pass

@app.get("/pet/{pet_id}", status_code=200)
def get_pet_by_id(
    pet_id: UUID
) -> Pet:
    pass

@app.put("/pet/{pet_id}", status_code=202)
def get_pet_by_id(
    pet_id: UUID,
    pet: Pet
) -> Pet:
    pass

@app.delete("/pet/{pet_id}", status_code=204)
def get_pet_by_id(
    pet_id: UUID
) -> None:
    pass