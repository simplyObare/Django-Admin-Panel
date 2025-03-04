from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class Course(models.Model):

    COURSE_STATUS = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=120)
    description = models.TextField()
    publish_date = models.DateTimeField()
    price = models.FloatField()
    author = models.CharField(max_length=200)
    status = models.CharField(
        max_length=15,
        choices=COURSE_STATUS,
        default="published",
        help_text="Enter field documentation",
    )

    def __str__(self):
        return self.title


#  @property
#  def lessons(self):
#      return self.lesson_set.all().order_by("position")


class Lesson(models.Model):
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_urls = models.CharField(max_length=1000)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def image_preview(self):
        return mark_safe(f'<img src="{self.image.url}" alt="" width="150" />')

    image_preview.short_description = "Image"

    def admin_image_preview(self):
        return mark_safe(
            f'<img src="{self.image.url}" alt="" width="95" height="100" style="border-radius: 50%; border: 1px solid #242424" />'
        )

    admin_image_preview.short_description = "Image"

    def __str__(self):
        return self.name
