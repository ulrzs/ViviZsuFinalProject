import numpy as np

class Breadcrumb():
    def __init__(self, position, lifetime=600.0):
        self.position = np.array(position, dtype=float)
        self.lifetime = lifetime #time left before instantaneous combustion
        self.eaten = False

    def update(self, dt):
        self.lifetime -=  dt

    def is_expired(self):
        return self.lifetime <= 0 or self.eaten
    

     
