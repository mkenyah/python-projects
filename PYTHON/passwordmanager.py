from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)



def load_key(master_pwd):
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key + master_pwd.encode()

master_pwd = input("What is the master password?: ")

key = load_key(master_pwd)
fer = Fernet(key)

def view():
    with open("passwords.text", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, "password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.text', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view the existing ones (view, add), press q to quit: ").lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
        print("Viewing existing passwords...")
    elif mode == "add":
        add()
        print("Adding a new password...")
    else:
        print("Invalid mode 😥")
        continue
