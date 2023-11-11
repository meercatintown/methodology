from django.db import models
from django.db.models.functions import Cast
from django import forms

# Create your models here.

class Step(models.Model):
    title = models.CharField(max_length=200)
    step_number = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = [
            Cast("step_number", output_field=models.IntegerField()),
        ]

class Subtask(models.Model):
    step = models.ForeignKey(Step, related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    related_tools = models.ManyToManyField('tools.Tool', related_name='subtask', null=True)
    
    def tools_list(self):
        return list(self.related_tools.all())
    def __str__(self):
        return self.title
