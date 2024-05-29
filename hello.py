def hello_world():
	return "Hello World!"

# return the string "Hello World! Hello World! ... Hello World!" N times
def hello_world_n(N):
	str0 = "Hello World!"
	strN = str0
	for i in range(N-1):
		strN = strN + ' ' + str0
	return strN
