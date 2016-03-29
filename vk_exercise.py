import vk
import sqlite3

user_profile_url = 'https://vk.com/may.timur'


def write_to_db(data):
	c.executemany('INSERT INTO posts VALUES (?, ?, ?, ?, ?)', (data,))
	conn.commit()


def get_most_liked_url(user_profile_url):
	user_id = user_profile_url.split("/")[-1]
	user = api.users.get(user_ids=user_id, fields='domain')[0]
	user_domain = user['domain']
	wall_posts = api.wall.get(domain=user_domain)[1:]

	for i in range(len(wall_posts)):
		data = [wall_posts[i]['date'], 'https://vk.com/wall%s_%s' % (wall_posts[i]['from_id'],
			wall_posts[i]['id']), wall_posts[i]['likes']['count'], wall_posts[i]['comments']['count'],
			wall_posts[i]['reposts']['count']]
		write_to_db(data)

	wall_posts.sort(key=lambda i: i['likes']['count'])
	most_liked = wall_posts[-1]
	most_liked_url = 'https://vk.com/wall%s_%s' % (
		most_liked['from_id'], most_liked['id'])
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

	conn = sqlite3.connect('posts.db')
	c = conn.cursor()
	c.execute('''create table posts
	(date text, url text, likes text,
	comments text, reposts text)''')
	conn.commit()

	print(get_most_liked_url(user_profile_url))

	c.close()
	