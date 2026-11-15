import numpy as np

class Bird:
    def __init__(self, position, velocity, max_speed = 4.0):
        self.position = np.array(position, dtype = float)
        self.velocity = np.array(velocity, dtype = float)
        self.max_speed = max_speed
        self.heading = 0.0

    def limit_speed(self): 
        current_speed = np.linalg.norm(self.velocity)
        if current_speed > self.max_speed:
            self.velocity = self.velocity / current_speed * self.max_speed #create a unit vector then multiply by max speed to keep same direction


    def update_heading(self):
         if np.linalg.norm(self.velocity) > 0:
            self.heading = np.arctan2(self.velocity[1], self.velocity[0]) #arctan2 takes components separately and calculates the heading angle more reliably


    def compute_acceleration(self, world):
        raise NotImplementedError #pigeon and crow will ovveride this


