Richieste da effettuare su Postman in base alla funzione da richiamare:

get_users --> tipo = GET | body json = {"table_name": "accounts"} | endpoint = "/get_users"

insert_user --> tipo = POST | body json = {
    "table_name": "accounts",
    "username": "Frughy",
    "email": "frughy@dominio.it",
    "password": "10062004"
} | endpoint = "/insert_user"

remove_user --> tipo = DELETE | body json = {
    "table_name": "accounts",
    "user_id": "3"
} | endpoint = "/remove_user"

update_user --> tipo = PUT | body json =  {
	"table_name": "accounts",
    "username": "Frughy",
    "old_password": "10062004",
    "new_password": "1010"
} | endpoint = "/update_user"