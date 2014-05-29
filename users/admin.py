from django.contrib import admin
from users.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    exclude = ['date_created']

admin.site.register(User, UserAdmin)