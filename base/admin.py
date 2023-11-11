from django.contrib import admin

# Register your models here.

from .models import *
from tools.models import *
from vulnerabilities.models import *

admin.site.register(Step)
admin.site.register(Tool)
admin.site.register(Vulnerability)