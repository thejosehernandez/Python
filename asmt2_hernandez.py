import functs_hernandez

function = ['a','m','r','g','q']
hash ={}
decision = ''
theinput = ''
filename =input("Enter file to open: ")
fh = open(filename, "a+")
fh.seek(0)
string_line=fh.readlines()

for i in range(len(string_line)): 
	split_line = string_line[i].split(":")
	username = split_line[0]
	password = split_line[1].strip()
	hash[username]=password

while(decision != 'q'):
	while(1):
		print ("User accounts \n")
		print ("------------------------ \n")
		print ("a = Add new user account \n")
		print ("m = Modify existing user account \n")
		print ("r = Remove existing user account \n")
		print ("g = Generate list of accounts \n")
		print ("q = Quit \n")
		decision	= input("Enter choice: ")	
		if decision == 'q':
			break
		if decision in function:
			if decision == 'a':
				hash = functs_hernandez.add_user(hash)
			elif decision == 'm':
				hash = functs_hernandez.modify_user(hash)
			elif decision == 'r':
				hash = functs_hernandez.remove_user(hash)
			elif decision == 'g':
				hash = functs_hernandez.generate_list(hash)
		else:
			print("Wrong choice")
theinput = input("Save contents?: (y/n): ")
fh.close()

if(theinput == "y"):
	fh=open(filename,"w")
	for k,v in hash.items():
		print(k,v)
		s = k + ":" + v + "\n"
		fh.write(s)
fh.close()