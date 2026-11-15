import numpy as np
from entities.pigeon import Pigeon
from sim.world import World

rng = np.random.default_rng(42)  # fixed seed so runs are identical

N = 20
dt = 1.0
steps = 500

# Create the flock
pigeons = []
for _ in range(N):
    pos = rng.uniform(0, 100, size=2)
    vel = rng.uniform(-2, 2, size=2)
    pigeons.append(Pigeon(pos, vel))

# Set weights AFTER the pigeons exist
for p in pigeons:
    p.w_separation = 30.0
    p.w_cohesion = 0.02
    p.w_food = 3.0

# Create the world and give it the flock
world = World()
world.pigeons = pigeons
food_pos = np.array([100.0, 100.0])


def average_spread(flock):
    center = np.mean([p.position for p in flock], axis=0)
    distances = [np.linalg.norm(p.position - center) for p in flock]
    return np.mean(distances)


def order_parameter(flock):
    headings = []
    for p in flock:
        speed = np.linalg.norm(p.velocity)
        if speed > 0:
            headings.append(p.velocity / speed)
    return np.linalg.norm(np.mean(headings, axis=0))


for step in range(steps):
    # Drop the breadcrumb once
    if step == 100:
        world.add_breadcrumb(food_pos)

    # Phase 1: compute every acceleration BEFORE moving anyone
    accels = []
    for p in pigeons:
        accels.append(p.compute_acceleration(world))

    # Phase 2: apply them
    for p, acc in zip(pigeons, accels):
        p.velocity += acc * dt
        p.limit_speed()
        p.position += p.velocity * dt
        p.update_heading()

    # Phase 2b: eating and cleanup (temporary print to compare with earlier runs)
    crumbs_before = len(world.breadcrumbs)
    world.update_breadcrumbs(dt)
    if len(world.breadcrumbs) < crumbs_before:
        print(f"crumb eaten at step {step}")

    # Phase 3: measure
    if step % 10 == 0 and step >= 90:
        center = np.mean([p.position for p in pigeons], axis=0)
        print(f"step {step:3d}  distance to food = {np.linalg.norm(center - food_pos):.1f}  crumbs = {len(world.breadcrumbs)}")

    if step % 50 == 0:
        avg_speed = np.mean([np.linalg.norm(p.velocity) for p in pigeons])
        lonely = sum(1 for p in pigeons if len(world.get_neighbours(p)) == 0)
        print(f"step {step:3d}  spread = {average_spread(pigeons):.2f}  speed = {avg_speed:.2f}  order = {order_parameter(pigeons):.2f}  alone = {lonely}  crumbs = {len(world.breadcrumbs)}")