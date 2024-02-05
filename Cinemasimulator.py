films={
    "Frozen":{"Age":7, "seats_left":20}
    ,"Anabelle":{"Age":18, "seats_left":2}
    ,"Master":{"Age":13, "seats_left":0}
    ,"IT":{"Age":16, "seats_left":12}
    ,"Tangled":{"Age":5,"seats_left":1}
    }
while True:
    user_choice=input("What film would you want to watch?:").strip().title()
    if user_choice in films:
        
        age=int(input("How old are you?").strip())

        if age>=int(films[user_choice]["Age"]):
            if int(films[user_choice]["seats_left"])>0:
                print("Enjoy the film!")
                films[user_choice]["seats_left"]=str(int(films[user_choice]["seats_left"])-1)
            else:
                print("Sorry we are sold out!")
        else:
            print("You are too young to watch the film")
        
    else:
        print("We don't have that film")
