import vk

user_profile_url = 'https://vk.com/may.timur'

def bubblle(A):
	for j in range(len(A) - 1):
		for i in range(len(A) - 1):
			if A[i]['likes']['count'] > A[i + 1]['likes']['count']:
				A[i]['likes']['count'], A[i+1]['likes']['count'] = A[i+1]['likes']['count'], A[i]['likes']['count']
	return A


def get_most_liked_url(user_profile_url):
	user_id = user_profile_url.split("/")[-1]
	user = api.users.get(user_ids=user_id, fields='domain')
	user_domain = user[0]['domain']
	wall_posts = del api.wall.get(domain=user_domain)[0]
	wall_posts = bubblle(wall_posts)
	most_liked = wall_posts[-1]
	most_liked_url = 'https://vk.com/wall%s_%s' % (most_liked['from_id'], most_liked['id'])
	return most_liked_url


if __name__ == '__main__':
	try:
		with open('api.key', 'r') as api_key:
			app_id = api_key.readline()
			secret_key = api_key.readline()
	except:
		print('Put app_id and secret_key in api.key file')
	session = vk.AuthSession(app_id=app_id, scope=('offline, wall'))
	api = vk.API(session)

	print(get_most_liked_url(user_profile_url))


