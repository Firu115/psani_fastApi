import json
import re
import sqlite3

import bcrypt

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email) -> str:  # kontroluje jestli to je mail nebo jmeno
    if re.search(regex, email):
        return "email"
    else:
        return "jmeno"


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
    heslo = run(f'SELECT (hash_heslo) FROM uzivatele '
                f'WHERE {check(user.jmeno_nebo_email)} = "{user.jmeno_nebo_email}";')
    try:
        heslo = heslo[0][0][2:-1]  # odstraní [("b'hash'",)] abych to tam zas mohl přidat lol
    except IndexError:
        return "uziv"  # neexistuje takevoj uzivatel

    return bcrypt.checkpw(user.heslo.encode("utf8"), heslo.encode("utf8"))


def get_lekce():
    return run(f'SELECT * FROM lekce')


def get_splnene_lekce(email):
    dokoncene = run(f'SELECT dokonceno FROM uzivatele WHERE email = "{email}"')
    dokoncene = eval(dokoncene[0][0])
    vysledek = []
    for i in dokoncene:
        if len(get_cviceni_v_lekci(run(f'SELECT pismena FROM lekce WHERE id = "{i}"')[0][0])) == len(dokoncene[i]):
            vysledek.append(i)
    return vysledek


def get_splnene_cviceni_v_lekci(email, pismena_lekce):
    lekce_id = run(f'SELECT id FROM lekce WHERE pismena = "{pismena_lekce}";')[0][0]
    dokoncene = eval(run(f'SELECT dokonceno FROM uzivatele WHERE email = "{email}"')[0][0])[lekce_id]
    print(dokoncene)
    return dokoncene


def get_cviceni_v_lekci(pismena_lekce):
    lekce_id = run(f'SELECT id FROM lekce WHERE pismena = "{pismena_lekce}";')[0][0]
    return run(f'SELECT id, pismena, slova FROM cviceni WHERE cviceni.lekce_id = "{lekce_id}";')


def get_uziv_info(email):
    info = \
    run(f'SELECT id, email, jmeno, aktivni, prumerna_rychlost, prumerna_presnost, dokonceno FROM uzivatele WHERE email = "{email}"')[
        0]
    pocet_dokoncenych_cviceni = sum([len(v) for k, v in eval(info[6]).items()])
    pocet_cviceni = len(run(f'SELECT id FROM cviceni'))
    return {
        'jmeno': info[2],
        'email': info[1],
        'aktivni': info[3],
        'prumerna_rychlost': eval(info[4])[0],
        'prumerna_presnost': eval(info[5])[0],
        'dokonceno': round(pocet_dokoncenych_cviceni / pocet_cviceni * 100, 1)  # v procentech
    }
