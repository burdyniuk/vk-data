# Burdyniuk Ilya - vk api script - collect users data
import requests
import time
import json
import os
import os.path

def get_friends():
	token = "TOKEN"
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

			while(1):
				offset = 0
				try:
					friends = requests.get("https://api.vk.com/method/friends.get?user_id="+str(user_id)+"&fields=sex,bdate,city,country,photo_50,photo_100,photo_200_orig,photo_200,photo_400_orig,photo_max,photo_max_orig,online,online_mobile,lists,domain,has_mobile,contacts,connections,site,education,universities,schools,can_post,can_see_all_posts,can_see_audio,can_write_private_message,status,last_seen,common_count,relation,relatives,counters&offset="+str(offset)+"&v=5.103&access_token="+token)
					result = friends.json()
				except ValueError:
					print("Error")

				if "error" in result:
					f = open("./links/"+str(user_id)+".json", "w")
					json.dump("", f)
					f.close()
					break

				if "response" in result:
					f = open("./friends/"+str(user_id)+".json", "a+")
					json.dump(result, f)
					f.close()

					f = open("./links/"+str(user_id)+".json", "a+")
					for friend in result["response"]["items"]:
						f.write(str(friend["id"])+" ")
					f.close()

					if result["response"]["count"] == 5000:
						offset += 5000
					else:
						break
				else:
					f = open("./links/"+str(user_id)+".json", "w")
					json.dump("", f)
					f.close()

				time.sleep(1)
