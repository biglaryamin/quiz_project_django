from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User



UserAdmin.fieldsets += (
    ("Additional Fileds",{'fields':('is_author','special_user')}),
)

admin.site.register(User,UserAdmin)