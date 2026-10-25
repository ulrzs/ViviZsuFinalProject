# Urban Pigeon Flock & Crow Simulator

An interactive computer simulation of a flock of city pigeons navigating a park, rushing for breadcrumbs, and dodging a mischievous hooded crow. 

This project explores how simple individual decisions create lifelike group behavior, tests different math algorithms used to calculate motion, and visualizes the results with 2D graphics.

---

## What is This Project About?

If you watch pigeons in a city square, no single bird is in charge—yet they fly, turn, and scatter together as a cohesive group. 

In this project, we:
- Program a swarm of pigeons where each bird follows three basic rules: don't crash into neighbors, fly in the same general direction as the flock, and stay reasonably close together.
- Add an interactive hooded crow that chases the pigeons, and let users click on screen to drop breadcrumbs that attract the birds.
- Compare three standard numerical calculation methods (**Euler**, **Verlet**, and **Runge-Kutta**) to see which one calculates bird movement most accurately without glitching or blowing up.
- Measure bird flight speeds across the flock to see if crowded animal swarms follow the same statistical patterns as heated gas molecules.
- Render actual bird sprites that turn and tilt smoothly to match the direction they are flying.

---

## How It Works Behind the Scenes

### 1. Bird Behavior Rules (The Swarm Engine)
Every frame, each pigeon decides how to steer based on a few basic forces:
- **Separation:** Steer away from nearby birds to prevent overlapping or mid-air crashes.
- **Alignment:** Look at immediate neighbors and match their average flight direction.
- **Cohesion:** Steer toward the center of the nearby group so birds don't get lost alone.
- **Breadcrumb Attraction:** Move toward food dropped by the user.
- **Crow Evasion:** Scatter and fly in the opposite direction when the crow swoops too close.

To keep the computer from slowing down when checking hundreds of birds, we use a fast spatial search algorithm (**k-d tree**) so birds only check the neighbors right next to them.

### 2. Calculating Motion (The Math Solvers)
Computers calculate movement in tiny steps of time ($\Delta t$). We compare three different calculation algorithms to update the birds' positions:
1. **Forward Euler Method:** The simplest method. It works fine for quick tests, but can quickly become inaccurate and cause birds to unnaturally accelerate or fly off-screen over time.
2. **Velocity-Verlet:** A stable, physics-friendly method that keeps energy balanced and prevents long-term drift.
3. **Runge-Kutta 4th Order (RK4):** A high-precision method that samples multiple points per time step to calculate smooth, reliable flight paths.

### 3. Data & Graphs
- **Order vs. Chaos:** We add random steering "noise" to see at what point a synchronized flock breaks down into unorganized, random wandering.
- **Speed Distributions:** We collect the speeds of all birds over time and test whether their speed patterns match standard thermodynamic bell curves (the Maxwell-Boltzmann distribution).

---

## Requirements & Installation

- **Language:** Python 3.10+
- **Key Libraries:** `numpy`, `scipy`, `matplotlib`

### Quick Setup

```bash
# Clone the repository
git clone [https://github.com/your-username/pigeon-flocking-simulator.git](https://github.com/your-username/pigeon-flocking-simulator.git)
cd pigeon-flocking-simulator

# Install required Python packages
pip install numpy scipy matplotlib