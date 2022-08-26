# Generated by Django 4.0.5 on 2022-08-01 03:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ApiServer', '0010_category_alter_post_options_alter_post_like_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='top_news',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
