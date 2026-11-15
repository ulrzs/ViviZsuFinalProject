import numpy as np
from entities.breadcrumb import Breadcrumb


class World:
    def __init__(self, size=200.0, margin=30.0, boundary_strength=0.3):
        self.size = size
        self.margin = margin
        self.boundary_strength = boundary_strength
        self.pigeons = []
        self.breadcrumbs = []
        self.crow = None          # placeholder until the Crow exists
        self.eat_radius = 5.0


    def add_breadcrumb(self, position):
        self.breadcrumbs.append(Breadcrumb(position))

    def get_neighbours(self, bird):
        result = []
        for pig in self.pigeons:
            if pig is bird:
                continue
            if np.linalg.norm(pig.position - bird.position) < bird.perception_radius:
                result.append(pig)
        return result
    
    def boundary_force(self, bird):
        force = np.zeros(2)
        for axis in range(2):
            if bird.position[axis] < self.margin:
                force[axis] = self.boundary_strength
            elif bird.position[axis] > self.size - self.margin:
                force[axis] = -self.boundary_strength
        return force
        

    def update_breadcrumbs(self, dt):
        for crumb in self.breadcrumbs:
            for p in self.pigeons:
                if np.linalg.norm(p.position - crumb.position) < self.eat_radius:
                    crumb.eaten = True
            crumb.update(dt)
        self.breadcrumbs = [c for c in self.breadcrumbs if not c.is_expired()]