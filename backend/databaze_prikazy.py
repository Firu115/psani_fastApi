import re
import sqlite3

import bcrypt

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    if re.search(regex, email):
        return True
    else:
        return False


def run(query):
    sqliteConnection = sqlite3.connect('databaze.db')
    cursor = sqliteConnection.cursor()
    cursor.execute(query)

    vysledek = cursor.fetchall()

    sqliteConnection.commit()
    cursor.close()
    sqliteConnection.close()

    return vysledek


def uzivatel_do_db(user):
    run(f'INSERT INTO uzivatele (jmeno, email, hash_heslo) '
        f'VALUES ("{user.jmeno}","{user.email}", "{bcrypt.hashpw(user.heslo, bcrypt.gensalt())}");')


def get_jmeno_by_email(email):
    return run(f'SELECT jmeno FROM uzivatele WHERE email = "{email}"')


def get_email_by_jmeno(jmeno):
    return run(f'SELECT email FROM uzivatele WHERE jmeno = "{jmeno}"')


def check_uziv(user):
    if check(user.jmeno_nebo_email):  # pokud je to email
        heslo = run(f'SELECT (hash_heslo) FROM uzivatele '
                    f'WHERE email = "{user.jmeno_nebo_email}";')[0][0][2:-1]
        # odstraní b'...' abych to tam zas mohl přidat lol

    else:  # pokud je to jmeno
        heslo = run(f'SELECT (hash_heslo) FROM uzivatele '
                    f'WHERE jmeno = "{user.jmeno_nebo_email}";')[0][0][2:-1]

    return bcrypt.checkpw(user.heslo.encode("utf8"), heslo.encode("utf8"))


def get_lekce():
    return run(f'SELECT * FROM lekce')
