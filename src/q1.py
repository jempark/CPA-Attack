import numpy as np 
import matplotlib.pyplot as plt

fp = open("traces.txt", "r")

oneLine = fp.readline().split(" ")
oneLine = np.array(oneLine, np.int)

plt.plot(oneLine)
plt.xlabel("Samples")
plt.ylabel("Voltage")
plt.title("Plot of Power Trace")
plt.show()

