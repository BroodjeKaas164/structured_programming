userList = ['joe', 'sue', 'hani', 'sophie']

print("Sign in")
username = input("Username: ")

if username in userList:
    print("Token Authenticated!")
else:
    print("Token Invalid!")

print("Done!")