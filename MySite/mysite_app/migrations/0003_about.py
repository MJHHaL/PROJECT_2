# Generated by Django 4.1.6 on 2023-02-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite_app', '0002_rename_mainpage_mainmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('about_content', models.TextField()),
            ],
        ),
    ]
