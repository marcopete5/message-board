from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from registration.forms import RegistrationForm
from registration.backends.simple.views import RegistrationView


def message_view(request):
    messages = Message.objects.all()
    context = {}
    context['messages'] = messages

    if request.method == 'POST':

        comment_body = request.POST.get('comment_body', None)
        message = request.POST.get('message', None)
        user = request.POST.get('user', None)


        print comment_body
        print message
        print user

        current_user = User.objects.get(username=user)
        current_message = Message.objects.get(id=message)

        Comment.objects.create(body = comment_body, user=current_user, message=current_message)

    return render(request, 'message.html', context)


def post_view(request):
	messages = Message.objects.all()
	context = {}
	context['messages'] = messages
	if request.method == 'POST':

		message_body = request.POST.get('message_body', None)
		# title = request.POST.get('title', None)
		user = request.POST.get('user', None)

		print message_body
		# print title
		print user

		current_user = User.objects.get(username=user)

		Message.objects.create(body=message_body, user=current_user)

	return render(request, 'post.html', context)

# def signup(request):
# 	if request.method == 'POST':
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			username = request.POST['username']
# 			password = request.POST['password1']

# 			print username
# 			print password

# 			user = authenticate(username=username,password=password) 

# 			print user

# 			if user is not None:
# 				print "user is not None"
# 				if user.is_active:
# 					print "user is active"
# 					login(request, user)
# 					return HttpResponseRedirect('/message/')
# 			else: 
# 				return HttpResponseRedirect('/login/')


# 	else:
# 		form = UserCreationForm()

# 	return render(request, 'sign_up.html', {'form':form})







class SignUp(RegistrationView):
	form_class = CreateUserForm
	template_name = 'sign_up.html'


	# def get(self, request, *args, **kwargs):
	# 	form = self.form_class(initial=self.initial)
	# 	return render(request, 'sign_up.html', {'form':form})

	# def post(self, request, *args, **kwargs):
	# 	form = self.form_class(request.POST)
	# 	if form.is_valid():

	# 		return HttpResponseRedirect('/message/')

	# 	return render(request, 'sign_up.html', {'form': form})



	

