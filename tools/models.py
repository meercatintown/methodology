from django.db import models
from base.models import Step

# Create your models here.

class ToolTopic(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Tool(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    topic = models.ForeignKey(ToolTopic, on_delete=models.SET_NULL, null=True)
    step = models.ForeignKey(Step, related_name='%(class)s_tool_related_step', on_delete=models.CASCADE, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
