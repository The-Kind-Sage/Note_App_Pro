import os

# Creating necessary functions

def create_file():
    c_file = str(input("Enter the file name you want to create: "))
    your_note= str(input("Write your note: \n"))
    with open('note.txt','w') as newfile:
        newfile.write(your_note)

def display_file():
    with open('note.txt','r') as newfile:
        print(newfile.read())


def update_file():
    updated_note= str(input("Your New list\n"))
    with open('note.txt','a') as newfile:
        newfile.write(" "+updated_note)


def delete_file():
    del_file = str(input("Enter your file name: "))
    if del_file == create_file
    try:
        os.remove('note.txt')
        print("Your file has been deleted")
    except  FileNotFoundError: 
        print("Your file does not exists")




while 2>1:
    # User Dashboard
    
    print("\n****************\n*** NOTE APP ***\n****************\n")
    print("MENU: \n")
    print("1. Create a new Note")
    print("2. Add note to existing Note")
    print("3. View Note")
    print("4. Delete your Note")
    print("5. EXit\n")

    choice= int(input("ENter your choice(1-5): "))
    if choice== 1:
        create_file()

    elif choice== 2:
        update_file()

    elif choice== 3:
        try:
            display_file()
        except FileNotFoundError:
                print("No Note found, Create a New Note first ")

    elif choice== 4:
        delete_file()

    elif choice== 5:
        print("Exiting program...")
        break
    else:
        print("Please enter a valid choice")


        








