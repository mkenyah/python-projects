import random

def account():
    name = input("Full name: ")
    id_number = input("ID Number: ")

    if name and id_number:
        random_account_no = random.randint(111111111, 999999999)
        random_pin_no = random.randint(1111, 9999)
        credentials(name, id_number, random_account_no, random_pin_no)

def credentials(name, id_number, random_account_no, random_pin_no):
    with open("credentials.txt", 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"ID Number: {id_number}\n")
        file.write(f"Account Number: {random_account_no}\n")
        file.write(f"PIN Number: {random_pin_no}\n")
        file.write("\n")

        print("__________________________*ACCOUNT SUCCESSFULLY CREATED*_____________________ \n")
        print("*************HERE ARE YOUR ACCOUNT DETAILS*************** \n")
        print("Name: ", name ,"\n")
        print("ID Number:", id_number,"\n")
        print("This is your Account Number:", random_account_no,"\n")
        print("Your pin Number: ", random_pin_no,"\n")

while True:
    account()
    
    choice = input("\t\t Choose the account type (Saving/Fixed/Current): ").lower()
    
    if choice == "saving" or choice == "fixed" or choice == "current":
        with open("credentials.txt", 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 5):
                saved_name = lines[i].split(":")[1].strip()
                saved_id = lines[i + 1].split(":")[1].strip()

                if name == saved_name and id_number == saved_id:
                    print("Account Found:")
                    print(lines[i].strip())
                    print(lines[i + 1].strip())
                    print(lines[i + 2].strip())
                    print(lines[i + 3].strip())
                    break
            else:
                print("Account not found.")

    another_account = input("Do you want to create another account? (yes/no): ").lower()
    if another_account != 'yes':
        break
