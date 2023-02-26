from rocketpy import Rocket, SolidMotor, Flight

Engine = SolidMotor(
    thrustSource="PATH_TO_FILE",
    burnOut=1.62,
    grainNumber=4,
    grainSeparation=7/1000,
    grainDensity=1600,
    grainOuterRadius=20/1000,
    grainInitialInnerRadius=10/1000,
    grainInitialHeight=240/1000,

    nozzleRadius=11/1000,
    throatRadius=5.5/1000,
    interpolationMethod='linear'
)

CHKN = Rocket(
    motor=Engine,
    radius=58/1000,
    mass=2-0.42,
    inertiaI=6.60,
    inertiaZ=0.0351,
    distanceRocketNozzle=-1.255,
    distanceRocketPropellant=-0.85704,
)

CHKN.setRailButtons([0.2, -0.5])

NoseCone = CHKN.addNose(length=0.55829, kind="vonKarman", distanceToCM=0.71971)

FinSet = CHKN.addFins(4, span=0.100, rootChord=0.120, tipChord=0.040, distanceToCM=-1.04956)

Tail = CHKN.addTail(topRadius=0.0635, bottomRadius=0.0435, length=0.060, distanceToCM=-1.194656)

TestFlight = Flight(rocket=CHKN, environment=Env, inclination=92, heading=0)
TestFlight.allInfo()
