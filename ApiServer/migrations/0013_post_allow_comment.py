# Generated by Django 4.0.5 on 2022-08-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiServer', '0012_alter_post_options_post_snippet_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Allow_comment',
            field=models.BooleanField(default=True),
        ),
    ]
