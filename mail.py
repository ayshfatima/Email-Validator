email_address = input("Enter your email : ")
spaces,a,b = 0,0,0
if len(email_address)>=6:
    # print('We are proceeding for our second test')
    if email_address[0].isalpha():
        # print("we are proceeding for our third test")
        if ("@" in email_address) and (email_address.count("@")==1):
            if(email_address[-4]==".") ^ (email_address[-3]=="."):
                if(email_address.count(".")==1):
                    for i in email_address:
                        if i==i.isspace():
                            spaces=1
                        elif i.isdigit():
                            continue
                        elif i.isalpha():
                            if i==i.upper():
                                a=1
                        elif (i =="_") or (i==".") or (i=="@"):
                            continue
                        else:
                            b=1
                            
                            
                            
                    if spaces>=1 or a>=1 or b>=1:
                        print("Invalid check on spaces/operators/uppercase")
                    
                        
                else:
                    print("Invalid check on 2 or more dot operator")
            else:
                print("Invalid check on dot operator")
        else:
            print("Invalid email address : watch on @")
    else:
        print("Invalid email address : start with alphabet")
    
else:
    print("Invalid")
    
print(f" {email_address}")
