from django.urls import path
from base.views import *
from .views import *

urlpatterns = [
    path('', tools, name='tools'),
    path('<int:tool_id>/', tool, name='tool'),
    path('add_tool', add_tool, name='add_tool'),
    path('<int:tool_id>/edit_tool/', edit_tool, name='edit_tool'),
    path('<int:tool_id>/delete_tool/', delete_tool, name='delete_tool'),
]