##### Create a dataset containing user details #####

import csv

header = ['user_id', 'password']

data = [{'user_id' : 'Beining',
         'password' : '28748'},
        {'user_id' : 'Adam',
         'password' : '2381741'},
        {'user_id' : 'Sarah',
         'password' : '199AS'}] ### Can be improved by adding the order details for each user

with open('userDetail.csv', 'w', encoding='UTF8', newline='') as userDetail:
    writer = csv.writer(userDetail)
    writer.writerow(header)
    writer.writerows(data)
    

##### register and login #####

import pandas as pd

class LoginSystem:
    def __init__(self, ID, password): # Let the user input his/her ID and password
        self.ID = ID
        self.password = password
        self.userInfo = data
    
    
    # Check if the ID matches with any of the IDs in the data when logging in
    def login_checkID(self):
        for user in data:
            if user['user_id'] == self.ID:
                return True
        print("The user ID does not exist.")
        return False
    
    
    # Check whether the password is correct for the input ID
    def checkPassword(self):
        for user in data:
            if user['user_id'] == self.ID:
                user_password = user['password']
                return True
        return False
        print("Incorrect Password!")
    
    
    # Check whether the new ID already exist in the data
    def register_checkID(self):
        for user in data:
            if user['user_id'] == self.ID:
                user_password = user['password']
                print("The user ID already exist.")
                return True
        return False
    
    
    # Login
    def login(self):
        while not(self.login_checkID()):
            print("Please enter your ID again:")
        
        while not(self.checkPassword()):
            print("Please enter your Password again:")
        
        print("Logging in ... ...")
    
    
    # Register
    def register(self):
        while self.register_checkID():
            print("Please enter your ID again:")
        
        # store the new user info into the file system
        new_user = {'user_id' : self.ID,
                    'password' : self.password}
        self.userInfo.append(new_user, ignore_index=True)
        self.userInfo.to_csv("userDetail.csv", index=False) # write into file
        

##### Create a fuction that run the Login System and take the ID and password from users #####
def login_register():
    # take the ID and password from users
    ID = input("Please enter your user ID:")
    password = input("Please enter your password:")
    
    user = LoginSystem(ID, password)
    
    # Let the user choose whether he want login or register
    choice = input("Login or Register:")
    
    # Direct to Login system or Resgister system depend on user's choice
    if choice == "Login":
        user.login()
    if choice == "Register":
        user.register()
