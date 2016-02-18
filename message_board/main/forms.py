from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class CreateUserForm(forms.ModelForm):
	username=forms.CharField(max_length=30)
	password1=forms.CharField(max_length=30,widget=forms.PasswordInput()) #render_value=False
	password2=forms.CharField(max_length=30,widget=forms.PasswordInput())
	email=forms.EmailField(required=False)
	class Meta:
		model = User 
		fields = ['username', 'password1', 'password2', 'email']


	def clean_username(self): # check if username dos not exist before
		try:
			User.objects.get(username=self.cleaned_data['username']) #get user from user model
		except User.DoesNotExist :
			return self.cleaned_data['username']

		raise forms.ValidationError("this user exist already")


	def clean(self): # check if password 1 and password2 match each other
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:#check if both pass first validation
			if self.cleaned_data['password1'] != self.cleaned_data['password2']: # check if they match each other
				raise forms.ValidationError("passwords dont match each other")

		return self.cleaned_data


	def save(self): # create new user
		new_user=User.objects.create_user(username=self.cleaned_data['username'],
										password=self.cleaned_data['password1'],
										email=self.cleaned_data['email'],
											)
		# user = authenticate(username=self.cleaned_data['username'],password=self.cleaned_data['password1'])
		# if user is not None:
		# 	if user.is_active:
		# 		login(self, user)

		return new_user