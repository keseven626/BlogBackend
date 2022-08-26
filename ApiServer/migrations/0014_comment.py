# Generated by Django 4.0.5 on 2022-08-24 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiServer', '0013_post_allow_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiServer.post')),
            ],
        ),
    ]
