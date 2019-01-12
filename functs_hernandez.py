import re
#Add Function========================================
def add_user(local_hash):
	username =  input("Enter Username to Add: ")
	username = re.sub(r'\W+','',username)
	username = username.lower()
	if username in local_hash:
		print ("Username already exists in records! \n")
		return local_hash
	else:
		password = input("Enter Password: ")
		password = password.replace('\'','')
		local_hash[username] = password
	return local_hash

#Modify Function======================================
def modify_user(local_hash): 
	username = input("Enter the username to modify: \n")
	username = re.sub(r'\W+','',username)
	username = username.lower()
	if username not in local_hash:
		print ("Username does not exist in records \n")
		return local_hash
	current_password = input("Enter the current password: ")
	current_password = current_password.replace('\'','')
	if current_password == local_hash[username]:
		new_password = input("Enter a new password: ")
		local_hash[username] = new_password
	return local_hash
	
#Remove Function======================================
def remove_user(local_hash):
	username = input ("Enter the username to remove: ")
	username = re.sub(r'\W+','',username)
	username = username.lower()
	if username in local_hash:
		del(local_hash[username])
	else: 
		print("Wrong Username")
	return local_hash

#Generate Function====================================
def generate_list(local_hash):
	for k,v in local_hash.items():
		print (k + ":" + v )
	return local_hash