import requests, json

def get_url(user_name):
	return "https://api.github.com/search/repositories?q={}&sort=stars&order=desc".format(user_name)


def get_data(request, user_name):
	url = get_url(user_name)
	r = requests.get(url)
	data =  r.json()
	return data

def get_repo_content_url(owner, repo_name):
	return "https://api.github.com/repos/"+owner+'/'+repo_name+"/contents/"

def get_repo_contents(request, owner, repo_name):
	url = get_repo_content_url(owner, repo_name)
	r = requests.get(url)
	data =  r.json()
	return data

