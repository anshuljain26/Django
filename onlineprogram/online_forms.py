
from pagedown.widgets import PagedownWidget
from django import forms
from .models import project_category, Project,Upload, Enroll


class online_form(forms.ModelForm):
	Description = forms.CharField(widget=PagedownWidget)
	Publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Project
		fields=[
           'category',
           'title',
           'Description',
           'image',
           'Course_period',
           'cost',
           'Publish',



		]

class Upload_form(forms.ModelForm):
	Publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Upload
		fields = [
        'category_upload',
        'title_upload',
        'Content',
        'Video',
        'Publish',
    
		]

class enrollform(forms.ModelForm):
	name =   forms.CharField(max_length=220,widget=forms.TextInput(attrs={'type':'hidden','value':'abc'}))
	project = forms.CharField(label='Email address',widget=forms.TextInput(attrs={'type':'hidden','value':'abc'}))

	class Meta:
		model=Enroll
		fields=[
         'name',
         'project'
		 ]

