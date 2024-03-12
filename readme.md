get_users
Tipo: GET
Body JSON:
json
Copy code
{
    "table_name": "accounts"
}
Endpoint: /get_users
insert_user
Tipo: POST
Body JSON:
json
Copy code
{
    "table_name": "accounts",
    "username": "Frughy",
    "email": "frughy@dominio.it",
    "password": "10062004"
}
Endpoint: /insert_user
remove_user
Tipo: DELETE
Body JSON:
json
Copy code
{
    "table_name": "accounts",
    "user_id": "3"
}
Endpoint: /remove_user
update_user
Tipo: PUT
Body JSON:
json
Copy code
{
    "table_name": "accounts",
    "username": "Frughy",
    "old_password": "10062004",
    "new_password": "1010"
}
Endpoint: /update_user