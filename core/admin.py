from django.contrib import admin
from .models import *


admin.site.site_header = "Custom Admin Panel"
admin.site.site_title = "Custom Admin"

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
