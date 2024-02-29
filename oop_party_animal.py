class PartyAnimal: #to define the class
    
    def __init__(self): #method to initialize it. It takes self as a parameter
        self.x = 0 #x is the only attribute that we have
        
    def party(self): #method to call. It takes self as a parameter. self here is an alias of an and thats how u get to the instance. so self.x is the same as an.x and x is the attribute of the instance
        self.x = self.x + 1 #x is the only attribute that we have
        print('so far', self.x)
        
an = PartyAnimal() #this constructs it. this will not run the print. we have to call it which is done in the next line

an.party() #calls the party method
an.party()
an.party()

PartyAnimal.party(an)