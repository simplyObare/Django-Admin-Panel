from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(models.Model):
   last_name = models.CharField(max_length=130)
   first_name = models.CharField(max_length=130)
   course = models.ManyToManyField('Course', blank=True)
   
   class Meta:
      verbose_name_plural = 'people'
      
   def __str__(self):
      return f'{self.first_name} {self.last_name}'


class Course(models.Model):
   name = models.CharField(max_length=130)
   year = models.IntegerField()
   
   class Meta:
      unique_together = ('name', 'year')
      
   def __str__(self):
      return f'{self.name} {self.year}'

class Grade(models.Model):
   person = models.ForeignKey(Person, on_delete=models.CASCADE)
   course = models.ForeignKey(Course, on_delete=models.CASCADE)
   grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
   
   def __str__(self):
      return f'{self.person}, {self.course}: {self.grade}'