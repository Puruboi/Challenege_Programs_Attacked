# Project-0-Traffic_Python

Our problem is set in the traffic snarls of planet Lengaburu. After the recent Falicornian war, 
victorious King Shan of Lengaburu wishes to tour his kingdom. But the traffic in Lengaburu is killing.
 You should see how Silk Dorb gets jammed in the evening! Write code to help King Shan navigate Lengaburu's traffic

Problem : mission impossible King Shan wants to visit the suburb of Hallitharam, and has 2 possible orbits and 
3 possible vehicles to choose from.
Your coding challenge is to determine which orbit and vehicle King Shan should take to reach Hallitharam the fastest.

#Orbit options: 
#Orbit 1 - 18 mega miles & 20 craters to cross 
#Orbit 2 - 20 mega miles & 10 craters to cross 
#Vehicle options: 
#Bike - 10 megamiles/hour & takes 2 min to cross 1 crater 
#Tuktuk - 12 mm/hour & takes 1 min to cross 1 crater 
#Car - 20 mm/hour & takes 3 min to cross 1 crater
#Weather conditions (affects the number of craters in an orbit):
#Sunny - craters reduce by 10%. Car, bike and tuktuk can be used in this weather. 
#Rainy - craters increase by 20%. Car and tuktuk can be used in this weather. 
#Windy - no change to number of craters. Car and bike can be used in this weather

# Your program should take the location to the test file as parameter. Input needs to be read from a text file, 
# and output should be printed to the console. 
# WEATHER ORBIT_1_TRAFFIC_SPEED ORBIT_2_TRAFFIC_SPEED VEHICLE_NAME ORBIT_NO
# Input Format
# RAINY 40 25 CAR ORBIT2

Note: A vehicle cannot travel faster than the traffic speed for an orbit. So even though a car’s max speed is 20 megamiles/hour, it 
can only go at 10 megamiles/hour if that is the traffic speed for that orbit. Also, if there is a tie in which vehicle to choose, use bike, 
auto,car in that order
