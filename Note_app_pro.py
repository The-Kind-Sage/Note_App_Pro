import os

# Creating necessary functions

def create_file():
    c_file = str(input("Enter the file name you want to create: "))
    your_note= input("Write your note: \n")
    while True:
        file_location = input("Enter the location where you want to save this file: ")
        if os.path.exists(file_location):
            full_path = os.path.join(file_location, c_file)
            with open(full_path,'w') as newfile:
                newfile.write(your_note)
            print(f"Note saved at {full_path}")
            break
        else:
            print("Location does not exist, Please Try Again")
            

# def create_file():
#     c_file = input("Enter the file name you want to create: ")
#     your_note = input("Write your note: \n")
#     while True:
#         file_location = input("Enter the location where you want to save this file: ")
#         if os.path.exists(file_location):
#             full_path = os.path.join(file_location, c_file)
#             with open(full_path, 'w') as newfile:
#                 newfile.write(your_note)
#             print(f"Note saved at {full_path}")
#             break
#         else:
#             print("Location does not exist, Please Try Again")

    
        


def update_file():
    u_file_location = (input("Enter the location where your file exist: "))
    if os.path.exists(u_file_location):
        u_file = (input("Enter the file name you want to update: "))
        if os.path.exists(u_file):
                updated_note= str(input("Your New Note: \n"))
                with open(u_file,'a') as newfile:
                    newfile.write(" "+updated_note)
        else:
             print("File name does not exist, Please Try Again")
    
    else:
         print("Location does not exist, Please Try Again")


def display_file():
    with open(c_file,'r') as newfile:
        print(newfile.read())



def delete_file():
    del_file = str(input("Enter your file name: "))
    if del_file == create_file:
        try:
            os.remove(del_file)
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


        








