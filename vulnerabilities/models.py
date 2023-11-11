from django.db import models
from base.models import *
# Create your models here.

class VulnerabilityLevel(models.IntegerChoices):
    LOW = 1, 'Low'
    MID = 2, 'Mid'
    HIGH = 3,'High'

class VulnerabilityStack(models.IntegerChoices):
    UNDEFINED = 0, 'Undefined'
    SECURITY = 1, 'Security'
    NETWORK = 2, 'Network'
    SYSTEM =  3, 'Operating System'
    DATABASE = 4, 'Database'
    SERVER = 5, 'Web Server'
    THIRD_PARTY = 6, 'Third Party Components'
    CUSTOM_WEB_APPS = 7, 'Custom Web Applications'

class Vulnerability(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    vuln_level = models.IntegerField(default=VulnerabilityLevel.MID, choices=VulnerabilityLevel.choices)
    stack = models.IntegerField(default=VulnerabilityStack.UNDEFINED, choices=VulnerabilityStack.choices, null=True)
    step = models.ForeignKey(Step, related_name='%(class)s_vuln_related_step', on_delete=models.CASCADE, default=0)
    
    def __str__(self):
        return self.title
