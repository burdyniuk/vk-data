# Burdyniuk Ilya - vk api script - collect users data
import requests
import time
import json
import os
import os.path

def get_members(group_id):
	token = "TOKEN"
	offset = 0

	while 1:
		print(offset)
		followers = requests.get("https://api.vk.com/method/groups.getMembers?group_id="+group_id+"&fields=sex,bdate,city,country,photo_50,photo_100,photo_200_orig,photo_200,photo_400_orig,photo_max,photo_max_orig,online,online_mobile,lists,domain,has_mobile,contacts,connections,site,education,universities,schools,can_post,can_see_all_posts,can_see_audio,can_write_private_message,status,last_seen,common_count,relation,relatives,counters&count=1000&offset="+str(offset)+"&v=5.103&access_token="+token)
		members = followers.json()

		if os.path.exists("./members"):
			pass
		else:
			os.mkdir("./members")

		# save .json files with info of every member
		for member in members["response"]["items"]:
			if os.path.exists("./members/"+str(member["id"])+".json"):
				pass
			else:
				f = open("./members/"+str(member["id"])+".json", "w")
				json.dump(member, f)
				f.close()

		# offset update 
		if members["response"]["items"]:
			if len(members["response"]["items"]) == 1000:
				offset += 1000
			else:
				break
		time.sleep(1)
