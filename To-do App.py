from sqlite3 import Cursor, connect


uid = int(input("Enter Your ID Number: "))
print(f"Your User ID Is: {uid}")
db = connect("Database.db")
cr = db.cursor()
cr.execute(
    "CREATE TABLE if not exists 'Todos' (name text,user_id integer)")


##################################################################
input_message = """
What Do You Want To Do ?
"s" => Show All todos
"a" => Add New todo
"d" => Delete A todo
"q" => Quit The App
Choose Option: 
"""
##################################################################


def commit_and_close():
    # Save (Commit) Changes
    db.commit()

# Close Database
    db.close()
    print("Connection To Database Is Closed")

#####################################


def show_todos():
    cr.execute(f"select * from Todos where user_id={uid}")
    if len(cr.fetchall()) == 0:
        print("You have not added any todos yet")
    else:
        cr.execute(
            f"SELECT name,user_id from Todos WHERE user_id={uid}")
        print(f"Your User ID Is: {uid}")
        print("="*60)
        print(f"Todos : ")
        for row in cr.fetchall():
            print(row[0])
        print("="*60)
        print("Operation done successfully")

#####################################


def add_todo():

    while True:
        print("Type (q) If You Want To Go Back To Main Menu")
        sk_name = input("todo Name: ").capitalize()

        if sk_name.lower() == "q" or sk_name.lower() == "quit":
            break
        cr.execute(
            f"INSERT INTO Todos (name,user_id) VALUES ('{sk_name}','{uid}')")
        db.commit()
        print("todo Added")
        print("="*60)

    #####################################


def delete_todo():

    sk = input("Write todo Name: ").strip().capitalize()
    cr.execute(f"delete from Todos where name = '{sk}' and user_id = '{uid}'")
    db.commit()
    print(f"todo {sk} Deleted Successfully")

#####################################


def update_todo():

    sk = input("Write todo Name: ").strip().capitalize()
    print("New", end=" ")
    checker.check()
    db.commit()
    print(f"todo {sk} Updated Successfully")


##################################################################
commands = ["s", "a", "d", "u", "q"]
while True:
    print("="*60)

    user_input = input(input_message).strip().lower()
##################################################################
    if user_input in commands:
        #####################################

        if user_input == "s":
            print("="*60)
            show_todos()
            break
#####################################
        elif user_input == "a":
            print("="*60)

            add_todo()
#####################################
        elif user_input == "d":
            print("="*60)

            delete_todo()
#####################################
        elif user_input == "u":
            print("="*60)

            update_todo()
#####################################
        elif user_input == "q":

            break
#####################################
    else:
        print(f"Sorry This Command \"{user_input}\" Is Not Found")
##################################################################
commit_and_close()
print("="*60)
