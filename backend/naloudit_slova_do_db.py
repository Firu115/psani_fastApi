import sqlite3

sqliteConnection = sqlite3.connect('databaze.db')
cursor = sqliteConnection.cursor()

cviceni = cursor.execute(f'SELECT id, pismena, slova FROM cviceni ORDER BY lekce_id;').fetchall()
slova_ze_slovniku = cursor.execute(f'SELECT id, slovo FROM slovnik;').fetchall()
print(cviceni)

probrane_pismena = ''
for cvic in cviceni:
    print(cvic)
    if cvic[1] is not None:
        probrane_pismena += cvic[1]
    else:
        slova = ''

        for slovo in slova_ze_slovniku:
            for pismeno in slovo[1]:
                if pismeno not in probrane_pismena:
                    break
            else:
                slova += slovo[1] + ','
                # cursor.execute(f'DELETE FROM slovnik WHERE id = "{slovo[0]}"').fetchall()

        print(slova)
        if slova == '':
            cursor.execute(f'UPDATE cviceni SET slova = NULL WHERE id = "{cvic[0]}";').fetchall()
        else:
            slova = list(slova.split(","))[:-1]
            for i in slova:
                for j in cursor.execute(f'SELECT id, pismena, slova FROM cviceni ORDER BY lekce_id;').fetchall():
                    if (j[1] is not None) and (i in j[1]):
                        print("odebiram")
                        try: slova.remove(i)
                        except: pass
            cursor.execute(f'UPDATE cviceni SET slova = "{slova}" WHERE id = "{cvic[0]}";').fetchall()


sqliteConnection.commit()
sqliteConnection.close()
