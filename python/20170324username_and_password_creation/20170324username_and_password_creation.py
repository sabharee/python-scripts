users={}
status=""
while status != "q":
    status = raw_input("already registered user y/n or Press q to quit: ")  

    if status == "n":
         create_user = raw_input("new username: ")

         if create_user in users: 
             print "username is already exist"

         else:
             create_password = raw_input("new password: ")
             users[create_user] = create_password
             print "user successfully created"     

    elif status == "y": 
        login = raw_input("enter username: ")

        if login in users:
           password = raw_input("enter password: ")
           print

           if login in users and password in users:
               print "login successful"
        else:
            print
            print("user doesn't exist")
if status == "q":
    print "logout successful"     
