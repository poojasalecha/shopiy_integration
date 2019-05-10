from __future__ import unicode_literals

import uuid
import datetime

from django.db import models
from django.utils.translation import pgettext_lazy


class RepoDetails(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	owner = models.CharField(pgettext_lazy(' entry field', 'Owner Name'),max_length=256, null=True)
	repo_name = models.CharField(pgettext_lazy('entry field', 'Repo Name'), max_length=256, null=True)
	stars_count = models.IntegerField(pgettext_lazy('entry field', 'Stars Count'), null=True)

	def __str__(self):
		return self.repo_name

	class Meta:
		ordering = ('stars_count', 'repo_name')


class Packages(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    package_name = models.CharField(pgettext_lazy(' entry field', 'Package Name'),max_length=256, default='', blank=True)
    repo = models.ForeignKey(RepoDetails, related_name="repo_package", blank=True, null=True)
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.by_user)


















    