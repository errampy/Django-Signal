from django.contrib import admin
from SignalApp1.models import *
# Register your models here.
class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone_no','address','create_at']
admin.site.register(EmployeeDetails,EmployeeDetailsAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','notify_user','notify_user_time_stamp','active']

admin.site.register(BlogPost,BlogPostAdmin)