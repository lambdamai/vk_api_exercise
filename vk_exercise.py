#!/usr/bin/python
# -*- coding: utf-8 -*-
import vk

def get_most_liked_url(user_profile_url):
	session = vk.AuthSession(app_id=app_id, scope="offline,wall")
	api = vk.API(session)
	user_domain = "lambda_it"
	user = api.users.get(users_id=user_domain)
	wall_posts = api.wall.get(domain=user_domain)
	most_liked = 0
	most_liked_url = []
	for i in range(1,len(wall_posts)):
		if wall_posts[i]["likes"]["count"] > most_liked:
			most_liked_url = "https://vk.com/" + user_domain + "?w=wall" + str(wall_posts[i]["to_id"]) + "_" + str(wall_posts[i]["id"])
			most_liked = wall_posts[i]["likes"]["count"]
	return most_liked_url

try:
	with open('api.key', 'r') as f:
		app_id = f.readline()
		secret_key = f.readline()
except:
	print("Put app_id and secret_key in file api.key")

user_profile_url = "https://vk.com/lambda_it"

if __name__ == "__main__":
	print(get_most_liked_url(user_profile_url))
