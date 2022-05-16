class Model:

    #Creating an array to keep all objects in the game
    self.entities = []


    #Defining a variable to keep track of the gamestate
    self.status = None

    #The constructor for the model
    def __init__(self):
        self.status = "starting position"

