import sys
import matplotlib.pyplot as plt
# CONSTANTS
GRAV = 9.807
FREE_STREAM_DENSITY = 1.225
DRAG_COEFFICIENT = 0.6

# input variables
vi = 20
vf = 7
A_parachute = 0.18
M_nosecone = 0.3
M_rocket = 1.5

# prompt user
if (len(sys.argv) > 1 and sys.argv[1] == "ask"):
    vi = float(input("[?] Initial velocity before touchdown: "))
    vf = float(input("[?] Desired final velocity: "))
    A_parachute = float(input("[?] Parachute area: "))
    M_nosecone = float(input("[?] Nosecone mass: "))
    M_rocket = float(input("[?] Rest of rocket mass (w/o propellant): "))


def getAcceleration(v_c, m_r):
    F_d = DRAG_COEFFICIENT * 0.5 * FREE_STREAM_DENSITY * (v_c ** 2) * A_parachute
    return GRAV - (F_d / (M_nosecone + m_r))


dt = 0.001
vel = vi
time_elapsed = 0
chord = 0

time_axis = []
vel_axis = []
chord_axis = []

# rope changes calculations
m_rope = 0
vel_r = vi
chord_r = 0
vel_axis_rope = []
chord_axis_rope = []

while (vel > vf):
    vel += getAcceleration(vel, 0)*dt
    time_elapsed += dt
    chord += vel * dt

    time_axis.append(time_elapsed)
    vel_axis.append(vel)
    chord_axis.append(chord)

    vel_r += getAcceleration(vel, m_rope)*dt
    chord_r += vel_r * dt
    vel_axis_rope.append(vel_r)
    chord_axis_rope.append(chord_r)

    m_rope += vel * dt * 0.01


print('\n')
print("[+] Time needed to decelerate: ", time_elapsed, "s")
print("[+] Length of chord needed: ", chord, "m")

plt.plot(chord_axis, vel_axis, label="ignore rope mass")
plt.plot(chord_axis_rope, vel_axis_rope, label="rope mass taken into account")
plt.xlabel("Chord length (m)")
plt.ylabel("Impact Velocity (ms^-1)")
plt.title("Recovery Graph")
plt.legend()

plt.show()
