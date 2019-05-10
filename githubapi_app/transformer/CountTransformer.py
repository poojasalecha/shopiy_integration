""" transform data and return """
def transform(data):
	return {
		'forksCount': data['forks_count'],
		'starCount': data['star_count'],
		'repoName': data['repo_name'],
		'owner':data['owner']
	}