films={
    "Frozen":{"Age":"7", "seats_left":"20"}
    ,"Anabelle":{"Age":"18", "seats_left":"2"}
    ,"Master":{"Age":"13", "seats_left":"0"}
    ,"It":{"Age":"16", "seats_left":"12"}
    ,"Tangled":{"Age":"5","seats_left":"1"}
    }
while True:
    user_choice=input("What film would you want to watch?:").strip().title()
    if user_choice in films:

        #check user age
        
        age=int(input("How old are you?").strip())
        if age >  int(films[user_choice]["Age"]): # compare int and int , by default our dict was having string 
            

            #check seat available
            if int(films[user_choice]["seats_left"])>0:    #convert to int for comparison error was basically that we can not compate using <, >  across int and str
                print("Enjoy the film!")
                films[user_choice]["seats_left"]=str(int(films[user_choice]["seats_left"])-1)   # we make updated integer and store by converting back to int
        else:
            print("You are too young to watch the film")
        
    else:
        print("We don't have that film")
