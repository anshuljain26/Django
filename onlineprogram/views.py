from django.shortcuts import render, get_object_or_404, redirect

from .online_forms import online_form,Upload_form,enrollform

from django.contrib.auth import ( authenticate,login,logout,)

from .signup_form import UserloginForm,UserRegisterForm

from django.contrib import messages

from django.db.models import Q

from .models import project_category,Project,Upload,Enroll

from datetime import datetime
# Create your views here.




def Home(request):
	request.session.set_test_cookie()

	project=project_category.objects.all()
	context={
	'project':project
	}

	response  = render(request,'onlineprogram/online-index.html',context)


	return response






def admin_panel(request):
	form = online_form(request.POST or None,request.FILES or None)
	context={
        'form':form,
        'title':'Upload-Course'

		}

	if form.is_valid():
		instance=form.save(commit=False)
		#print(instance.title)
		print(instance.image.url)
		instance.save()
		

		return redirect('/online/adminupload')

	return	render(request,'onlineprogram/admin.html',context)





def admin_panel_upload(request):
	form=Upload_form(request.POST or None, request.FILES or None)
	context={
	 'form':form,
	 'title':'Video Upload'
	}

	if form.is_valid():
		instance =form.save(commit=False)

		instance.save()

		return redirect('/online')

	return render(request,'onlineprogram/admin-upload.html',context)




def projects(request):
	instances = Project.objects.all().order_by('-timestamp')
	query=request.GET.get('q')
	if query:
		instances=instances.filter(Q(title__icontains=query)|
			Q(category__categories__icontains=query)|
			Q(cost__icontains=query)).distinct()

	#print(instances)
	context={
	 'instances':instances,
	 'title':'Projects'

	}

	return render(request,'onlineprogram/projects.html',context)







def project_list(request,title=None):
	instances=Upload.objects.filter(title_upload__title=title)
	context={
      'instances':instances,
      'title':title

	}

	return render(request,'onlineprogram/project_list.html',context)







def category_list(request,category=None):
	instances=Project.objects.filter(category__categories=category)
	#print(instances)
	context={
	 'instances':instances,
	 'category':category
	}

	return render(request,'onlineprogram/category.html',context)







def enroll_project(request,title=None):
	instances=get_object_or_404(Project,title=title)
	already_enroll=Enroll.objects.filter(project=title,name=request.user)
	if len(already_enroll)>0:
		exists='exists'
	else:
		exists='not exists'
		


	#print(already_enroll)
	form =enrollform(request.POST or None)
	context={
	'form':form,
	'title':'Project-Enroll',
	'instances':instances,
	'exists':exists
	}
	if form.is_valid():
		print('YES')
		enroll_info=form.save(commit=False)
		enroll_info.name=request.user
		enroll_info.project=title
		print(enroll_info.name)
		print(enroll_info.project)
		enroll_info.save()

		return redirect('/online/projects')

	return render(request,'onlineprogram/enroll.html',context)
		



def profile(request,name=None):
	instance=Enroll.objects.filter(name=name)
	context={
    'instance':instance,
    'profile':'profile'

	}

	return render(request,'onlineprogram/profile.html',context)




def login_views(request):
	title = "Login"
	form = UserloginForm(request.POST or None)
	if form.is_valid():
	    username = form.cleaned_data.get("username")
	    password = form.cleaned_data.get('password')
	    user = authenticate(username=username, password=password)
	    #messages.warning(request, 'Your account expires in three days.')
	    
	    login(request,user)
	    return redirect("/online/")
	return render(request, "onlineprogram/signup.html", {"form":form, "title": title})






def register_views(request):
	if request.session.test_cookie_worked():
		print 'test cookie worked<<<'
	form = UserRegisterForm(request.POST or None)

	context={
	'title':'Register',
	'form':form
	}

	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, Password=password)

		return redirect('/online/')

	return render(request, "onlineprogram/signup.html", context)	





def logout_views(request):
    logout(request)
    return redirect("/online")













