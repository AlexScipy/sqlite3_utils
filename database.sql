DROP TABLE IF EXISTS accounts;

CREATE TABLE accounts (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        username    TEXT NOT NULL CHECK(length(username) <= 50),                       -- Limita la lunghezza massima a 50 caratteri
        email       TEXT NOT NULL UNIQUE CHECK(length(email) <= 255),                  -- Limita la lunghezza massima a 255 caratteri
        password_    TEXT NOT NULL CHECK(length(password_) <= 20),                       -- Limita la lunghezza massima a 20 caratteri
        created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at  DATETIME );--DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- non supportato in sqlite3, quindi creo un trigger sotto

                                                                                        -- Vincolo per la complessità della password
                                                                                        --CHECK(password REGEXP '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
                                                                                        -- Questo vincolo richiede almeno una lettera minuscola,
                                                                                        -- una maiuscola, un numero e una lunghezza minima di 8 caratteri per la password.


-- Crea un trigger chiamato "update_accounts_updated_at" che viene eseguito dopo ogni operazione di aggiornamento sulla tabella "accounts"
CREATE TRIGGER update_accounts_updated_at
AFTER UPDATE ON accounts
FOR EACH ROW
BEGIN
    -- Aggiorna il campo "updated_at" con la data/ora corrente per la riga che è stata aggiornata
    UPDATE accounts
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = OLD.id; -- Utilizza "OLD.id" per fare riferimento all'id della riga prima dell'aggiornamento
END;
