# Generated by Django 4.2.5 on 2023-11-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_alter_tool_step'),
        ('base', '0013_remove_step_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='related_tool',
            field=models.ManyToManyField(null=True, related_name='subtask', to='tools.tool'),
        ),
    ]
