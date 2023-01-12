import sqlite3

sqliteConnection = sqlite3.connect('backend/databaze.db')


def zeZalohyDo():
    slova = []

    fr = open('slova.csv', 'r', encoding="utf8")
    for i in fr.readlines():
        slova.append(i[:-1])

    # print(slova)
    fr.close()
    # fw = open('slova.csv', 'w', encoding="utf8")

    # for i in slova:
    # fw.write(i.lower() + ",")
    # fw.write('\n')

    # fw.close()

    return slova


def doDatabaze(i, slovo):
    cursor = sqliteConnection.cursor()

    try:
        cursor.execute(f'INSERT INTO slovnik VALUES ("{slovo}", "{i}");')
    except:
        pass


def resetIndexu():
    global sqliteConnection
    cursor = sqliteConnection.cursor()

    slova = cursor.execute(f'SELECT * FROM slovnik;').fetchall()

    cursor.execute("DELETE FROM slovnik WHERE id != -1;")

    for i, slovo in enumerate(slova):
        print(i, slovo[0])
        cursor.execute(f'INSERT INTO slovnik VALUES ("{slovo[0]}", "{i}");')


resetIndexu()

sqliteConnection.commit()

sqliteConnection.close()
