from django.shortcuts import render
from .models import *
from django.views.generic import ListView

class MessageView(ListView):
	model = Message 
	template_name = "message.html"
	context_object_name = "message"


