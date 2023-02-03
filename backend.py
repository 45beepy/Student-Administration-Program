import sqlite3

def studentData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname test, Lastname text, Dateofbirth text, Gender text, Mobile text,PM1 text, Mid1 text, POM1 text)")
    con.commit()
    con.close()

def addStdRec(StdID, Firstname, Lastname, Dateofbirth, Gender, Mobile, PM1, Mid1, POM1):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?,?)", (StdID, Firstname, Lastname, Dateofbirth, Gender, Mobile, PM1, Mid1, POM1))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows =cur.fetchall()
    con.close()
    return rows

def deleteRec():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(StdID="", Firstname="", Lastname="", Dateofbirth="",Gender="",Mobile="",PM1="",Mid1="",POM1=""):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Lastname=? OR Dateofbirth=? OR Gender=? OR Mobile=? OR PM1=? OR Mid1=? OR POM1=?",(StdID, Firstname, Lastname, Dateofbirth, Gender, Mobile, PM1, Mid1, POM1))
    rows =cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,StdID="", Firstname="", Lastname="", Dateofbirth="",Gender="",Mobile="",PM1="",Mid1="",POM1=""):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?,Firstname=?, Lastname=?, Dateofbirth=?, Gender=?, Mobile=?, PM1=?,Mid1=?,POM1=?, WHERE id=?", (StdID, Firstname, Lastname, Dateofbirth, Gender, Mobile, PM1, Mid1, POM1, id))
    con.commit()
    con.close()




    
    








    






studentData()
