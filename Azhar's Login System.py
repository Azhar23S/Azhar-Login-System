import re

pat = "^[^0-9][a-zA-Z0-9_]+@[a-z]+\.[a-z]{1,3}$"
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&_])[A-Za-z\d@$!#%*?&_]{5,16}$"

def register(email):
    file = open("user_details.txt","a")
    
    if re.match(pat,email):
        password = input("Enter your Password: ")

        if re.match(reg,password):        
            file.write(email+","+password+"\n")
            file.close()
            print("Email/Username registered sucessfully !!!")

        else:
            print("Invalid Password")
            
    else:
        print("Invalid Email address")
    
def login(email,password):
    file = open("user_details.txt", "r")
    
    for i in file:
        a,b = i.split(",")
        b = b.strip()
            
        if(a==email and b==password):
            print("Login Successful !!!")
         
        elif(a==email and b!=password):
            print("Invalid Password")
            print("Forget Password?")
            confirm = input("Enter \'YES\' to continue: ").upper()

            if confirm == "YES":
                
                print("Do you want to Retrieve Password or Generate New Password?")
                retrieve = input("Enter \'Ret\' to Retrieve or \'New\' to Generate New Password: ").capitalize()
                
                if retrieve=="Ret":
                    mail = input("Enter your Email to proceed: ")
                    
                    if mail==a:
                        print(f"{b} is your Password")
                        
                    else:
                        print("Invalid Email address")

                elif retrieve=="New":
                    mail2 = input("Enter your Email to proceed: ")
                    
                    if mail2==a:
                        new = input("Generate New Password: ")
                        
                        if re.match(reg,new):
                            with open('user_details.txt', 'r') as file :
                                filedata = file.read()
                                
                            filedata = filedata.replace(b,new)
                            
                            with open('user_details.txt', 'w') as file:
                                file.write(filedata)
                                
                            file.close()
                            print(f"{new} is your New Password")
                            
                        else:
                            print("Invalid Password")
                            
                        
                    else:
                        print("Invalid Email address")
                        
                else:
                    print("Invalid Keys")
                    
            else:
                print("Invalid Keys")
        
    file.close()

print("Welcome to Azhar's Login System")
print("")

sign = input("Enter \'Register\' or \'Login\' to Proceed: ").capitalize()

if sign == "Register":
    print("Enter your Email Address and Password to Register")
    email = input("Enter your Email: ")
    register(email)

elif sign == "Login":
    email = input("Enter your Email: ")
    file1 = open("user_details.txt","r")
    readfile = file1.read()
    
    if email in readfile:
        password = input("Enter your Password: ")
        login(email,password)
        
    else:
        print("Sorry, this email address doesn't exist. Please Register...")

else:
    print("Enter Valid Keys")
