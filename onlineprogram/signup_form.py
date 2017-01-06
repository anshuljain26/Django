from django.contrib import messages
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )


User= get_user_model()

class UserloginForm(forms.Form):

	username    =   forms.CharField(max_length=220,widget=forms.TextInput(attrs={'size':'52','margin-top':'20'}))
	password    =   forms.CharField(widget=forms.TextInput(attrs={'size':'52','margin-top':'20','type':'Password'}))

	def clean(self,*args,**kwargs):

		username = self.cleaned_data.get('username')
		password  = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username,password=password)

			if not user:
				raise forms.ValidationError('this user doesnot exists')
			if not user.check_password(password):
				raise forms.ValidationError('Password is incorrect')
			if not user.is_active:
				raise form.ValidationError('User is not Active anymore')


		return super(UserloginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	username =   forms.CharField(max_length=220,widget=forms.TextInput(attrs={'size':'52','margin-top':'20'}))
	email = forms.EmailField(label='Email address',widget=forms.TextInput(attrs={'size':'52','margin-top':'20'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'size':'52','margin-top':'20','type':'Password'}))
	confirmpassword= forms.CharField(widget=forms.TextInput(attrs={'size':'52','margin-top':'20','type':'Password'}))

	class Meta:
		model=User
		fields=[
              'username',
              'email',
              'password',
              'confirmpassword'          

		]

	def clean(self,*args,**kwargs):
		email=self.cleaned_data.get('email')
		password=self.cleaned_data.get('password')
		confirmpassword=self.cleaned_data.get('confirmpassword')
		email_qs = User.objects.filter(email=email)

		if email_qs.exists():
			raise forms.ValidationError('Email already exist!!')
		if password!=confirmpassword:
			raise forms.ValidationError('Password does not match')
		return super(UserRegisterForm,self).clean(*args,**kwargs)	
			

		

			



				

				
