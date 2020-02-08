#!/usr/bin/env python

import os
import sys
import optparse

# we need to import some python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")


from sumolib import checkBinary  # Checks for the binary in environ vars
import traci


def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true", default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options


# contains TraCI control loop
def run():
    step = 0
    print("vehID time(*0.01s) x_speed y_speed x_pos y_pos", file = open("locations.txt", "a"))
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep(step+.01) # modify time step. time is in seconds

# IMPTT: the variable step has no relation to time inside the SUMO simulation, it is just a variable that we we use to keep track of time,
# and the command traci.simulationStep(step+0.1) means running the simulation at time = step + 0.1

        if step > 173: # by 173 seconds, all the vehicles enter the simulation
            for veh in traci.vehicle.getIDList():
                veh1 = str(veh).split(".")[1]
                print(veh1, int(step*100), traci.vehicle.getSpeed(veh), traci.vehicle.getLateralSpeed(veh), traci.vehicle.getPosition(veh)[0], traci.vehicle.getPosition(veh)[1], file = open("locations.txt", "a"))
        # print(traci.vehicle.getIDList())

        step += 0.01 # modify time step

    traci.close()
    sys.stdout.flush()


# main entry point
if __name__ == "__main__":
    options = get_options()

    # check binary
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # traci starts sumo as a subprocess and then this script connects and runs
    traci.start([sumoBinary, "-c", "circles.sumocfg",
                             "--tripinfo-output", "tripinfo.xml"])
    run()