# SRP Rocket Recovery Simulations
Simulations for single-parachute-dual-rope rocket recovery. 

![Figure 1](Figure_2.png)

## Dynamic Rope Mass Landing Simulation
Plot the length of rope by which the main rocket body should extend past the nosecone to approximate the impact velocity experienced by the nosecone (and thus payload inside) after the main body lands (at higher impact velocity).

![Figure 1](Figure_3.png)

## Rope-Mass-Negligable Simulation
Similair, but mass of rope is negligable allowing the simulation to run significantly faster. However, some precision is lost.

## How to run
Run the following commands in your terminal:
```shell
$ git clone git@github.com:stasostyk/SRP-Rocket-Recovery-Simulations.git
$ cd SRP-Rocket-Recovery-Simulations
$ pip install -r requirements.txt
```
Then simply run the file with:
```shell
$ py dynamic_mass_landing_simulation.py
```

### Parameters
Here are some useful parameters you can pass along to customize the simulation to your needs.

```shell
$ py dynamic_mass_landing_simulation.py --ask
```

To prompt for input parameters rather than using hard-coded values (for rapid changes).

```shell
$ ... --3D
```
To render a 3D model instead.

```shell
$ ... --3D-time
```

```shell
$ ... -dt 0.1 # use a time-step of 0.1 instead
```

