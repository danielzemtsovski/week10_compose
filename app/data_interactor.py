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
    sql = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
    cursor.execute(sql, (first_name, last_name, phone_number)) 
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id

def get_all_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT id, first_name, last_name, phone_number FROM contacts"
    cursor.execute(sql)
    rows = cursor.fetchall()
    contacts_list = []
    for row in rows:
        contact_objects = Contact(row[0], row[1], row[2], row[3])
        contacts_list.append(contact_objects)
    cursor.close()
    conn.close()
    return contacts_list
    

def update_contact(id, first_name, last_name, phone_number):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE contacts SET first_name=%s, last_name=%s, phone_number=%s WHERE id=%s"
    cursor.execute(sql, (first_name, last_name, phone_number, id))
    conn.commit()
    success = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return success

def delete_contact(id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM contacts WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    success = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return success
       