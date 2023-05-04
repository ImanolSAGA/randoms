import random as rand
import time

range_num= 10000000
start_time= 0


start_time= time.time_ns()

for _ in range(range_num): aux= rand.random()

result= int((time.time_ns() - start_time) * 0.000001)

print("end rand test in "+str(result)+" ms")


start_time= time.time_ns()

for _ in range(range_num): aux= time.time_ns()

result= int((time.time_ns() - start_time) * 0.000001)

print("end myrand test in "+str(result)+" ms")