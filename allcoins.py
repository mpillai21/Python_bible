import random

## Create an abstract class called coin
class Coin:
    ## Create a constructor for the abstract class with the dictionary packed
    def __init__(self,rare=False,clean=True,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare=rare
        self.is_clean=clean
        if self.is_rare==True:
            self.value=self.original_value*1.25
        else:
            self.value=self.original_value
        if self.is_clean==True:
            self.colour=self.clean_colour
        else:
            self.colour=self.rusty_colour

        
    ## Create the methods for the abstract class
    def rust(self):
        self.color=self.rusty_colour

    def clean(self):
        self.colour=self.clean_colour

    def flip(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)
        self.heads=choice
        
    ## Create a destructor for the abstract class
    def __del__(self):
        print("The coin was spent!")

    ## Decide how each coin must be named in the list
    def __str__(self):
        if self.original_value>=1.0:
            return "Rs {} Coin".format(int(original_value))

##Create classes that inherit this abstract class
            
    
class One_rupee(Coin):
    def __init__(self):
        data={
            "original_value":1.00,
            "rusty_colour":"brown",
            "clean_colour":"silver",
            "edges":1,
            "diameter":2.25,
            "thickness":3.15,
            "mass":9.5
            }
        ##call super(parent) class and unpack the data within
        ##the parent's init function
        super().__init__(**data)
class Two_rupee(Coin):
    def __init__(self):
        data={
            "original_value":2.00,
            "rusty_colour":"bluish",
            "clean_colour":"silvery-gold",
            "edges":1,
            "diameter":2.50,
            "thickness":3.50,
            "mass":9.8
            }
        ##call super(parent) class and unpack the data within
        ##the parent's init function
        super().__init__(**data)

class Five_rupee(Coin):
    def __init__(self):
        data={
            "original_value":5.00,
            "rusty_colour":"greenish",
            "clean_colour":"gold",
            "edges":1,
            "diameter":2.00,
            "thickness":3.00,
            "mass":12.5
            }
        ##call super(parent) class and unpack the data within
        ##the parent's init function
        super().__init__(**data)

class Ten_rupee(Coin):
    def __init__(self):
        data={
            "original_value":10.00,
            "rusty_colour":None,
            "clean_colour":"bronze",
            "edges":1,
            "diameter":3.15,
            "thickness":2.20,
            "mass":10
            }
        ##call super(parent) class and unpack the data within
        ##the parent's init function
        super().__init__(**data)
        ##Show polymorphism for rusting function
        def rust(self):
            self.color=self.clean_colour

coins=[One_rupee(),Two_rupee(),Five_rupee(),Ten_rupee()]

for coin in coins:
    arguments=[coin,coin.colour,coin.value,coin.diameter,coin.thickness,coin.edges,coin.mass]
    string="{}-Colour:{},Value:{},Diameter(cm):{},Thickness(cm):{},No. of edges:{},Mass(g):{}".format(*arguments)
    print(string)
    


