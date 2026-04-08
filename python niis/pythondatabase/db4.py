import sqlite3

# connect database
conn = sqlite3.connect("student.db")
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

conn.commit()

while True:

    print("\n===== STUDENT CRUD MENU =====")
    print("1. Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    # INSERT
    if choice == 1:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        cur.execute("INSERT INTO student VALUES(?,?,?)",(id,name,marks))
        conn.commit()

        print("Record Inserted Successfully")

    # SELECT
    elif choice == 2:
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()

        print("\nID   NAME   MARKS")
        print("-------------------")

        for r in rows:
            print(r[0], r[1], r[2])

    # UPDATE
    elif choice == 3:
        id = int(input("Enter ID to Update: "))
        marks = int(input("Enter New Marks: "))

        cur.execute("UPDATE student SET marks=? WHERE id=?",(marks,id))
        conn.commit()

        print("Record Updated Successfully")

    # DELETE
    elif choice == 4:
        id = int(input("Enter ID to Delete: "))

        cur.execute("DELETE FROM student WHERE id=?",(id,))
        conn.commit()

        print("Record Deleted Successfully")

    # EXIT
    elif choice == 5:
        conn.close()
        print("Program Closed")
        break

    else:
        print("Invalid Choice")