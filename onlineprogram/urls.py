from django.conf.urls import url, include
from .views import (
          Home,
          admin_panel,
          admin_panel_upload,
          login_views,
          register_views,
          logout_views,
          projects,
          project_list,
          enroll_project,
          profile,
          category_list,

	)



urlpatterns = [
    url(r'^$',Home,name="home"),
    url(r'^onlineadmin/$',admin_panel,name="admin-panel"),
    url(r'^adminupload/$',admin_panel_upload,name="admin-panel-upload"),
    url(r'^login/$',login_views,name='login'),
    url(r'^register/$',register_views,name='register'),
    url(r'^logout/$',logout_views,name='logout'),
    url(r'^projects/$',projects,name='projects'),
    url(r'^(?P<title>[\w-]+)/$', project_list, name='project_list'),
    url(r'^(?P<title>[\w-]+)/enroll/$',enroll_project,name='enroll_project'),
    url(r'^(?P<name>[\w-]+)/profile/$',profile,name='profile'),
    url(r'^(?P<category>[\w-]+)/list/$',category_list,name='category_list')



    ]