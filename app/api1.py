import data_interactor
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CreateContact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

@router.get("/contacts")
def get_Contact():
    contacts = data_interactor.get_all_contacts()
    return [c.contact_to_dict() for c in contacts]
