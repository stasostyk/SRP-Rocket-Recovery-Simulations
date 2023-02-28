# SRP Rocket Recovery Simulations
Simulations for single-parachute-dual-rope rocket recovery. 

![Figure 1](Figure_2.png)

## Dynamic Rope Mass Landing Simulation
Plot the length of rope by which the main rocket body should extend past the nosecone to approximate the impact velocity experienced by the nosecone (and thus payload inside) after the main body lands (at higher impact velocity).

## Rope-Mass-Negligable Simulation
Similair, but mass of rope is negligable allowing the simulation to run significantly faster. However, some precision is lost.

## Prompt vs. Preset Values
To run the program with hard-coded values in the code, simply run the desired file. This is if you want to run the same simulation many times without being prompted each time for values.

Alternatively, you may run:
```bash
$ py dynamic_mass_landing_simulation ask
```
to be prompted for parameters.
