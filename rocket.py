from rocketpy import Environment, Rocket, SolidMotor, Flight

Env = Environment(
    railLength=5.2,
    latitude=32.990254,
    longitude=-106.974998,
    elevation=1400,
    date=(2020, 3, 4, 12) # Tomorrow's date in year, month, day, hour UTC format
)

# Env.setAtmosphericModel(type='Forecast', file='GFS')

MyRocket = SolidMotor(
    thrustSource="""C:\\Users\\sosty\\Downloads\\SRP_standard_components\\SRP_standard_components\\SRM2020_March.eng""",
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

Calisto = Rocket(
    motor=MyRocket,
    radius=58/1000,
    mass=2-0.42,
    inertiaI=6.60,
    inertiaZ=0.0351,
    distanceRocketNozzle=-1.255,
    distanceRocketPropellant=-0.85704,
)

Calisto.setRailButtons([0.2, -0.5])

NoseCone = Calisto.addNose(length=0.55829, kind="vonKarman", distanceToCM=0.71971)

FinSet = Calisto.addFins(4, span=0.100, rootChord=0.120, tipChord=0.040, distanceToCM=-1.04956)

Tail = Calisto.addTail(topRadius=0.0635, bottomRadius=0.0435, length=0.060, distanceToCM=-1.194656)

TestFlight = Flight(rocket=Calisto, environment=Env, inclination=92, heading=0)
TestFlight.allInfo()
