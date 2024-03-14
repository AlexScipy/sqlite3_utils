Richieste da effettuare su Postman in base alla funzione da richiamare:

get_users --> tipo = GET | endpoint = "/get_users"

insert_user --> tipo = POST | body json = {
     "username": "ciccio",
    "email": "ciccio@dominio.it",
    "password": "10062004"
} | endpoint = "/insert_user"

remove_user --> tipo = DELETE | body json = {
    "username": "ciccio",
    "password": "4321"
} | endpoint = "/remove_user"

update_user --> tipo = PUT | body json =  {
    "username": "ciccio",
    "old_password": "10062004",
    "new_password": "4321"
} | endpoint = "/update_user"
