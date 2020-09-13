# Burdyniuk Ilya - vk api script - collect users data
import requests
import time
import json
import os
import os.path

def get_friends():
	token = "f3299f9b959903f726b72526b2a7240b8705a5b79ba413ebeb7f29488c7318bf79852c01f52c5a7677220" #Ya
	#token = "2abb3de2f0234f0bc6554bf1e36d89a01823c1285142ef2570e2c79422f90b4f246932aca3763a06554a9" #Iana
	#token = "09b7f8a4137ba7a83f9521b153296aff66c68729bac0e5a5d5878844671d473d89eb81fe8c9d627ab426c" #Roma
	offset = 0

	if os.path.exists("./friends"):
		pass
	else:
		os.mkdir("./friends")

	if os.path.exists("./links"):
		pass
	else:
		os.mkdir("./links")

	i = 0

	for user in os.listdir("./members"):
		if user == "." or user == ".." or user == ".DS_Store":
			continue
		else:
			user = "./members/"+user
			f = open(user, "r")
			user_data = json.load(f)
			user_id = user_data["id"]
			f.close()
			i+=1
			print(i,"/",len(os.listdir("./members")),"-",user_id)

			if os.path.exists("./links/"+str(user_id)+".json"):
				continue

			offset = 0
			while(1):
				#try:
				friends = requests.get("https://api.vk.com/method/friends.get?user_id="+str(user_id)+"&fields=sex,bdate,city,country,photo_50,photo_100,photo_200_orig,photo_200,photo_400_orig,photo_max,photo_max_orig,online,online_mobile,lists,domain,has_mobile,contacts,connections,site,education,universities,schools,can_post,can_see_all_posts,can_see_audio,can_write_private_message,status,last_seen,common_count,relation,relatives,counters&offset="+str(offset)+"&v=5.103&access_token="+token)
				result = friends.json()
				time.sleep(1)
				# except ValueError:
				# 	print("Error")

				if "error" in result:
					print(result["error"]["error_msg"], user_id)
					f = open("./links/"+str(user_id)+".json", "w")
					json.dump("", f)
					f.close()
					break

				if "response" in result:
					f = open("./links/"+str(user_id)+".json", "a+")
					for friend in result["response"]["items"]:
						f.write(str(friend["id"])+" ")
						# write friends data
						if os.path.exists("./members/"+str(friend["id"])+".json"):
							pass
						else:
							print("write "+str(user_id)+" => "+str(friend["id"])+" count = "+str(result["response"]["count"]))
							fr = open("./friends/"+str(friend["id"])+".json", "w")
							json.dump(friend, fr)
							fr.close()
					f.close()

					# if result["response"]["count"] == 5000:
					# 	offset += 5000
					# 	print("offset\n")
					# else:
					# 	print("Break")
					break
