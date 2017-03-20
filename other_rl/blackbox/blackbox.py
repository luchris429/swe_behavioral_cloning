#PYTHON 3
#NOT PYTHON 2

def scoreVal(state):
	if uin[0] == uin[1] and uin[1] == uin[2]:
		return -10
	elif uin[2] == "B" and uin[1] == "A":
		if uin[0] == "L":
			return 10
		return 2
	elif uin[2] == "B" and uin[1] == "L":
		if uin[0] == "M":
			return 20
		return 2
	elif uin[2] == "M" and uin[1] != "M":
		return 1
	elif uin[2] == "L" and uin[1] != "L":
		return 1
	else:
		return -1

uin = ["M","M","M"]
score = 0
val_ins = ["A","B","C","D"]
num_inputs = 30
for i in range(num_inputs):
	letter_in = input(str(i) + ": Next Input (A, B, C, or D): ")
	while(letter_in not in val_ins):
		print("Invalid Input")
		letter_in = input(str(i) + ": Next Input (A, B, C, or D): ")
	if(letter_in == "A"):
			uin.append("M")
	elif(letter_in == "B"):
			uin.append("L")
	elif(letter_in == "C"):
			uin.append("A")
	elif (letter_in == "D"):
		uin.append("B")
	uin.pop(0)
	score = score + scoreVal(uin)
	print("Observation: " + uin[0]+uin[1]+uin[2])
	print("Score: " + str(score))
print("Final Score: " + str(score))