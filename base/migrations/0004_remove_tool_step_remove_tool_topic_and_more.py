# Generated by Django 4.2.5 on 2023-09-23 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_tool_step'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='step',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Vulnerability',
        ),
        migrations.DeleteModel(
            name='Tool',
        ),
        migrations.DeleteModel(
            name='ToolTopic',
        ),
    ]
