


from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import *


class MyAdminSite(AdminSite):
    site_header = 'Real State'
    site_title  = 'Real State'
    index_title = 'Real State'
    # You can add on more attributes if you need 
    # Check out https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#adminsite-objects

# Create admin_site object from MyAdminSite
my_admin_site = MyAdminSite(name='Real State')



# Create and register all of your models
# ....

# This is the default Django Contrib Admin user / group object
# Add this if you need to edit the users / groups in your custom admin
my_admin_site.register(Group, GroupAdmin)
my_admin_site.register(User, UserAdmin)
my_admin_site.register(profileModel)