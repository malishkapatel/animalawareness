user_details = {'malishka' : '123' , 'arpita':'456' , 'ramya':'abc'}
user = input('whats your username')
password = input('enter your password')
getpass = user_details.get(user , "Username not found")
if password == getpass:
    print ('Login sucessful')
else:
    print ('One of them is incorrect')
    x = input('do you want to register? Type yes or no')
    if x== "yes" :
        user_details[user] = password
print (user_details)