# Generated by Django 4.0.5 on 2022-07-27 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiServer', '0007_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='draft', max_length=10),
        ),
    ]