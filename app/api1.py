import data_interactor
from fastapi import APIRouter , HTTPException
from pydantic import BaseModel

router = APIRouter()

class CreateContact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

@router.get("/contacts")
def get_contact():
    contacts = data_interactor.get_all_contacts()
    return [c.contact_to_dict() for c in contacts]

@router.post("/contacts")
def create(contact: CreateContact):
    new_id = data_interactor.create_contact(contact.first_name, contact.last_name, contact.phone_number)
    return {"message": "Contact created successfully", "id": new_id}

@router.put("/contacts/{id}")
def update(id: int, contact: CreateContact):
    success = data_interactor.update_contact(id, contact.first_name, contact.last_name, contact.phone_number)
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact updated successfully"}

@router.delete("/contacts/{id}")
def delete_contact(id: int):
    success = data_interactor.delete_contact(id)
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}