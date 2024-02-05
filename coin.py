class Rupee:
    ## create a constructor
    def __init__(self,rare=False):

        self.rare=rare
        if self.rare==True:
            self.value=5
            self.colour="gold"
        else:
            self.value=1
            self.colour="silver"
        self.num_edges=1
        self.diameter=22.5 #mm
        self.thickness=3.15 #mm
        self.heads=True
    ## Create a method to rust
    def rust(self):
        self.color="greenish"

    def clean(self,rare):
        self.rare=rare
        if self.rare==True:
            self.colour="gold"
        else:
            self.colour="silver"
    def flip(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)
        self.heads=choice
    ## Create a destructor
    def __del__(self):
        print("The coin was spent!")

    
    


