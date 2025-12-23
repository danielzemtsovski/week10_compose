import mysql.connector

class Contact:
    def __init__(self,id:int, first_name:str, last_name:str, phone_number:str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def contact_to_dict(self):
        return {"id":self.id,
                "first_name":self.first_name,
                "last_name":self.last_name,
                "phone_number":self.phone_number
                }
    
    def get_connection():
        return mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",         
            password="" ,
            database="contacts_db"
            )

    def create_contact(first_name, last_name, phone_number):
        conn = get_connection()
        cursor = conn.cursor()
        return  
    
    def get_all_contacts():
        return
    
    def update_contact(id, first_name, last_name, phone_number):
        return
    
    def delete_contact(id):
        return