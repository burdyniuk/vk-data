import csv
import os
import json
import os.path

def friendship_graph():
	#check if folder exists
	if os.path.exists("./graph"):
		pass
	else:
		os.mkdir("./graph")

	#initialize the csv file
	nodes = open('./graph/nodes.csv', 'w', newline='')
	writer = csv.writer(nodes)
	writer.writerow(["id", "label", "type", "link", "sex"])
	
	#open the files and write to nodes
	for subs in os.listdir("./members"):
		if subs == "." or subs == ".." or subs == ".DS_Store":
			continue
		f = open("./members/"+subs, "r")
		user = json.load(f)
		writer.writerow([user["id"], str(user["first_name"]+" "+user["last_name"]).strip(), "subscriber","https://vk.com/id"+str(user["id"]), user["sex"]])
		f.close()

	nodes.close()

	#create edges file
	edges = open('./graph/edges.csv', 'w', newline='')
	writer = csv.writer(edges)
	writer.writerow(["source", "target"])
	for friends in os.listdir("./friends"):
		if friends == "." or friends == ".." or friends == ".DS_Store":
			continue
		f = open(friends, "r")
		print(friends)
		data = f.read()
		ids = data.split()
		ident = friends.replace(".json","")
		for uid in ids:
			writer.writerow([ident, uid])
