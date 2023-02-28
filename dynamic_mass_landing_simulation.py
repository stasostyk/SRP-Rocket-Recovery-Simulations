import sys
import matplotlib.pyplot as plt
from colour import Color

# CONSTANTS
GRAV = 9.807
FREE_STREAM_DENSITY = 1.225
DRAG_COEFFICIENT = 0.6
dt = 0.001

# input variables
vi = 20
vf = 7
A_parachute = 0.18
M_nosecone = 0.3
M_rocket = 1.5

# prompt user
if ("--ask" in sys.argv):
    vi = float(input("[?] Initial velocity before touchdown: "))
    vf = float(input("[?] Desired final velocity: "))
    A_parachute = float(input("[?] Parachute area: "))
    M_nosecone = float(input("[?] Nosecone mass: "))
    M_rocket = float(input("[?] Rest of rocket mass (w/o propellant): "))


def getAcceleration(v_c, m_r):
    F_d = DRAG_COEFFICIENT * 0.5 * FREE_STREAM_DENSITY * (v_c ** 2) * A_parachute
    return GRAV - (F_d / (M_nosecone + m_r))



def getNextVelocity(vel_c, rope_length, rope_density, until_time):
    time_elapsed = 0
    vel = vel_c
    rope_left = rope_length

    while (time_elapsed < until_time):
        vel += getAcceleration(vel, rope_left * rope_density) * dt
        rope_left -= vel * dt
        time_elapsed += dt

    return vel


def generateImpactCurve(rope_density):
    vel = vi
    rope_length = 0
    time_elapsed = 0
    vel_axis = []
    rope_axis = []

    while (vel > vf and vel <= vi):
        time_elapsed += dt
        rope_length += vel * dt
        vel = getNextVelocity(vi, rope_length, rope_density, time_elapsed)

        vel_axis.append(vel)
        rope_axis.append(rope_length)
        # print("[+] At velocity " + str(vel))

    return rope_axis, vel_axis, time_elapsed, rope_density


def display(rope_axises, vel_axises, rope_densities, colours):
    print("[+] Rendering results... ")

    for i in range(len(rope_axises)):
        plt.plot(rope_axises[i], vel_axises[i], label="Rope Density: " + str(rope_densities[i]) + " kg/m^3", color=colours[i].rgb)

    plt.title("Difference Between Parachute Rope Length for Recovery Graph")
    plt.xlabel("Rope length ($m$)")
    plt.ylabel("Impact Velocity ($ms^-1$)")
    plt.title("Recovery Graph")
    plt.legend()
    plt.show()



def display3D(rope_axises, vel_axises, rope_densities, colours):
    print("[+] Rendering 3D results... ")
    fig = plt.figure()
    graph3D = fig.add_subplot(projection='3d')

    for i in range(len(rope_densities)):
        graph3D.scatter(rope_axises[i], vel_axises[i], [rope_densities[i] for z in range(len(rope_axises[i]))], color=colours[i].rgb)

    graph3D.set_title("Difference Between Parachute Rope Length for Recovery Graph")
    graph3D.set_xlabel("Rope Length ($m$)")
    graph3D.set_ylabel("Impact Velocity ($ms^-1$)")
    graph3D.set_zlabel("Density ($kgm^3$)")
    plt.show()



def main():
    rope_axises = []
    vel_axises = []
    rope_densities = []
    for i in range(5, 100, 5):
        rope_axis, vel_axis, time, rope_density = generateImpactCurve(i / 1000) # 000379
        rope_axises.append(rope_axis)
        vel_axises.append(vel_axis)
        rope_densities.append(rope_density)


    colours = list(Color("cyan").range_to(Color("blue"), len(rope_densities)))

    if ("--3D" in sys.argv):
        display3D(rope_axises, vel_axises, rope_densities, colours)
    else:
        display(rope_axises, vel_axises, rope_densities, colours)

    print('\n')
    print("[+] Time needed to decelerate: ", time, "s")
    print("[+] Length of chord needed: ", rope_axis[len(rope_axis)-1], "m")


if __name__ == "__main__":
    main()
