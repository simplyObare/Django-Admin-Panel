from django.db import models


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
