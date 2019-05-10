
""" local imports """
from .helpers import get_data, get_repo_contents
from .utils import Utils
from .basecontroller import BaseController
from transformer import CountTransformer
from .models import RepoDetails, Packages

""" djanngo imports """
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

import requests
import json, re


# Create your views here.

def get_repositories(request, username):
	data = get_data(request, username)
	if data:
		return BaseController().respond_with_success(200, 'Got the Repos', data=data)
	else:
		return BaseController().respond_with_success(200, 'No repos found', data={})

@csrf_exempt
def save_count_of_stars_forks(request, username):
	if request.method == 'POST':
		data =  get_data(request, username)
		star_fork = []
		for item in data['items']:
			forks_count = item['forks_count']
			star_count = item['stargazers_count']
			full_name = item['full_name']
			owner, repo_name = filter(None, re.split('/', full_name))
			star_fork.append({'owner': owner, 'repo_name':repo_name, 'star_count':star_count, 'forks_count':forks_count})
			repo_details, created = RepoDetails.objects.get_or_create(owner=owner, repo_name=repo_name)
			repo_details.stars_count = star_count
			repo_details.save()
		result, pagination_info = Utils().custom_pagination(request, star_fork)
		return BaseController().respond_with_paginated_collection(200, result, pagination_info, CountTransformer)
	else:
		return BaseController().respond_with_error(404, 'Method not found')

@csrf_exempt
def save_package(request, owner, repo_name):
	if request.method == 'POST':
		data = get_repo_contents(request, owner, repo_name)
		content_data = []
		if data:
			for content in data:
				file_name = content['name']
				if file_name == 'package.json':
					repo_details, created = RepoDetails.objects.get_or_create(owner=owner, repo_name=repo_name)
					content_data.append(content)
					file_data = content['download_url']
					json_data = requests.get(file_data).json()
					if json_data['devDependencies']:
						for key, value in json_data['devDependencies'].iteritems():
							Packages.objects.get_or_create(package_name=key,repo=repo_details)
					if json_data['dependencies']:
						for key,value in json_data['dependencies'].iteritems():
							Packages.objects.get_or_create(package_name=key,repo=repo_details)
			if content_data:
				return BaseController().respond_with_success(200, 'Have package.json', data=json_data)
			else:
				return BaseController().respond_with_success(200, 'This Project doesnot contain package.json')
	else:
		return BaseController().respond_with_error(404, 'Method not found')


def get_top_packages(request):
	if request.method == 'GET':
		packages = Packages.objects.values('package_name').annotate(the_count=Count('package_name'))
		print packages
		return BaseController().respond_with_success(200, 'Top 10')



			





