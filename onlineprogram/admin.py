from django.contrib import admin

# Register your models here.
from .models import Project,project_category,Upload,Enroll




admin.site.register(Project)


admin.site.register(project_category)


admin.site.register(Upload)


admin.site.register(Enroll)