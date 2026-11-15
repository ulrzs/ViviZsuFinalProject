from entities.bird import Bird
import numpy as np

class Pigeon(Bird):
    def __init__(self, position, velocity, max_speed=4.0):
        super().__init__(position, velocity, max_speed) # runs Birds setup first so pos, vel, max_s and heading already exist
        self.perception_radius = 50.0
        self.separation_radius = 15.0
        self.max_force = 0.5
        self.w_separation = 1.5
        self.w_alignment = 1.0
        self.w_cohesion = 1.0
        self.w_food = 0.0


    def separation(self, neighbours): # to avoid crowding push yourself this way, just gives the desired direction
        total = np.zeros(2)
        for pig in neighbours:
            offset = self.position - pig.position
            dist = np.linalg.norm(offset)
            if 0 < dist < self.separation_radius:      
                total += offset / dist**2
        return total


    def alignment(self, neighbours):
        if len(neighbours) == 0:
            return np.zeros(2)
        return np.mean([pig.velocity for pig in neighbours], axis=0) - self.velocity
    

    def cohesion(self, neighbours):
        if len(neighbours) == 0:
            return np.zeros(2)
        return np.mean([pig.position for pig in neighbours], axis=0) - self.position


    def compute_acceleration(self, world):
        neighbours = world.get_neighbours(self)
        sep = self.separation(neighbours)
        ali = self.alignment(neighbours)
        coh = self.cohesion(neighbours)
        food = self.seek_food(world.breadcrumbs)

        total = (self.w_separation * sep + self.w_alignment * ali + self.w_cohesion * coh + self.w_food * food)
                
        force_length = np.linalg.norm(total)
        if force_length > self.max_force:
            total = total / force_length * self.max_force

        return total + world.boundary_force(self)
    
    def seek_food(self, breadcrumbs):
        nearest = None
        nearest_dist = self.perception_radius

        for crumb in breadcrumbs:
            dist = np.linalg.norm(crumb.position - self.position)
            if 0 < dist < nearest_dist:
                nearest = crumb
                nearest_dist = dist

        if nearest is None:
            return np.zeros(2)
            
        return (nearest.position - self.position) / nearest_dist


