from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from .models import Person, Course, Grade


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "show_average")
    list_display_links = ("last_name", "first_name")
    ordering = ("-last_name", "first_name")

    def show_average(self, obj):
        result = Grade.objects.filter(person=obj).aggregate(avg=models.Avg("grade"))
        avg = round(result["avg"], 2) if result["avg"] is not None else None

        if avg is not None:
            color = "green"
            if avg < 90 and avg > 60:
                color = "blue"
            elif avg <= 60:
                color = "red"
            return format_html('<span style="color: {}">{}</span>', color, avg)
        return None

    show_average.short_description = "Average Grade"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Person)
# admin.site.register(Course)
# admin.site.register(Grade)
