import time
import os

padding = "0000000000000000000000000000000"
key = ""
for i in range(32):
	times = []
	for j in range(10):
		start = time.time()
		os.system("echo '" + key + str(j) + padding + "' | ./task > err")
		end = time.time()
		res = end - start 
		print(res)
		times.append(res)
	key = key + str(times.index(max(times)))
	padding = padding[0:-1]
	print(key)
print(key) 
