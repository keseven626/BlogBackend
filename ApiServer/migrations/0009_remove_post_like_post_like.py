# Generated by Django 4.0.5 on 2022-07-27 12:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ApiServer', '0008_post_like_alter_post_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
