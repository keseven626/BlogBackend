# Generated by Django 4.0.5 on 2022-08-25 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiServer', '0016_alter_comment_post_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='content',
        ),
    ]