# SUMO_Circular_Track

1. Makes a certain number of vehicles move around in a circular track generated in SUMO and edited in NETEDIT. A text file is generated that logs the actual location of the vehicles every 0.1 seconds (configurable).

2. To view the simulation in SUMO GUI, type `sumo-gui circles.sumocfg`. For just viewing the simulation, comment out the code in circles.py that generates the text file of vehicle locations as it slows down the simulation.

3. Before executing `circles.py`, convert circles.py to an executable program using `chmod +x circles.py`. Then type `./circles.py` which will bring up the sumo-gui. Then run the simulation from the gui and locations will start getting saved to the file.
