from sim.world import World
from entities.pigeon import Pigeon

w = World()
for pos in ([10, 100], [190, 100], [100, 10], [100, 190], [10, 10], [100, 100]):
    b = Pigeon(pos, [0, 0])
    print(pos, w.boundary_force(b))