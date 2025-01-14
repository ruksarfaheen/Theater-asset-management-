from abc import ABC, abstractmethod

class AbstractTheatre(ABC):
    def _init_(self,asset_name,location,projector, num_screen,cleaning,sound,security,seats,status):
        self.name=asset_name
        self.location=location
        self.projector=projector
        self.screen=num_screen
        self.cleaning=cleaning
        self.sound=sound
        self.security=security
        self.seats=seats
        self.status=status
        self.new_parking=[]
        self.new_food=[]

    @abstractmethod
    def display_details(self):
        pass