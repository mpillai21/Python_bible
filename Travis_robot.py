known_users=["Meena","Tim","Emma","Rose","Deep"]
while True:
    print("Hi, my name is Travis")
    user=input("What is your name?:").strip().capitalize()
    if user in known_users:
        print("Hello {}!".format(user))
        remove=input("Would you like to be removed from the system?(Y/N):").upper()
        
        if remove=="Y":
            known_users.remove(user)
        else:
            print("Great, I didn't want you to leave.")
    else:
        print("Hello {}!".format(user))
        print("Hmm but I don't think I have met you!")
        add=input("Would you like to be added to the system?(Y/N):").upper()
        if add=="Y":
            known_users.append(user)
        else:
            print("Oh, come back soon.")
    
