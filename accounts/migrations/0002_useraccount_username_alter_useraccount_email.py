# Generated by Django 4.0.5 on 2022-06-16 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='username',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(max_length=300, unique=True),
        ),
    ]
