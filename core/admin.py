from django.contrib import admin
from .models import *


admin.site.site_header = "Custom Admin Panel"
admin.site.site_title = "Custom Admin"


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "publish_date", "price", "full_name")
    list_display_links = ("publish_date", "price")
    # exclude = ("title", "price")
    # fields = (("title", "price"), "publish_date", "status", "author")
    # fieldsets = (
    #      (
    #          None,
    #          {
    #              "fields": ("title", "publish_date", "price"),
    #          },
    #      ),
    #      (
    #          "Extra Info",
    #          {
    #              "classes": ("collapse", "wide"),
    #              "fields": ("status", "author"),
    #              "description": "This is a new group",
    #          },
    #      ),
    #  )

    @admin.display(description="New Name")
    def full_name(self, obj):
        return f"{obj.title}-{obj.price}"

    # full_name.short_description = "CompleteName"


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Course, CourseAdmin)
# admin.site.register(Lesson)
