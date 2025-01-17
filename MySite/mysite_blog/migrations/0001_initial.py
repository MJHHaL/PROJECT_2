# Generated by Django 4.1.6 on 2023-02-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
