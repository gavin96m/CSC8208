class User():
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self,username,password):
        if self.username == username & self.password == password:
            print("Login success.")
        else:
            print("Error, please check username and password.")
