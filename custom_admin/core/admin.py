from django.contrib import admin
from .models import *


admin.site.site_header = "Custom Admin Panel"
admin.site.site_title = "Custom Admin"


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "publish_date", "price", "status", "author", "full_name")
    list_display_links = ("title",)
    list_editable = ("price", "status", "author")
    list_filter = ("title", "publish_date", "status")
    search_fields = ("title",)
    list_per_page = 3

    # ordering = ("title",)
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
    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("title",)
        else:
            return ("price",)

    @admin.display(description="New Name")
    def full_name(self, obj):
        return f"{obj.title}-{obj.price}"

    # full_name.short_description = "CompleteName"


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course")
    list_filter = ("course__status",)
    search_fields = ("course__price__gte",)
    # autocomplete_fields = ("course",)
    raw_id_fields = ("course",)


# Register your models here.
admin.site.register(Course, CourseAdmin)
# admin.site.register(Lesson)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "admin_image_preview")
    readonly_fields = ("image_preview",)
