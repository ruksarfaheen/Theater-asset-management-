from  AbstractTheatre import AbstractTheatre

class user(AbstractTheatre):
    
    def display_details(self):
        print("\nTheatre information:")
        print("\nTheatre name:",self.name)
        print("Theatre Location:",self.location)
        print("Projector type:",self.projector)
        print("number of screens:",self.screen)
        print("\nMaintenance Details:")
        print("\ncleaning and sanitation:",self.cleaning)
        print("sound system:",self.sound)
        print("security maintenance:",self.security)
        print("seats  available:",self.seats)
        print("status:",self.status)
        
        for parking in self.new_parking:
            print("\nAdditional Details:")
            print("Parking:",parking)
        for food in self.new_food:
            print("\nAdditional Details:")
            print("Food counter:",food)
        

    def set_name(self,new_name):
        self.name=new_name
        
    def set_location(self,new_location):
        self.location=new_location
        
    def set_projector(self,new_projector):
        self.projector=new_projector
        
    def set_screen(self,new_screen):
        self.screen=new_screen
        
    def set_cleaning(self,new_cleaning):
        self.cleaning=new_cleaning
        
    def set_sound(self,new_sound):
        self.sound=new_sound
        
    def set_security(self,new_security):
        self.security=new_security
        
    def set_seats(self,new_seats):
        self.seats=new_seats
        
    def set_status(self,new_status):
        self.status=new_status

    def add_parking(self,parking):
        self.new_parking.append(parking)
        
    def add_food(self,food):
        self.new_food.append(food)