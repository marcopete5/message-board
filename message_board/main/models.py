from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Message(models.Model):
	# title = models.CharField(max_length=300)
	body = models.TextField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.body

class Comment(models.Model):
	body = models.TextField()
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message)

	def __unicode__(self):
		return self.body

	def get_absolute_url(self):
		return reverse('main.views.message')



