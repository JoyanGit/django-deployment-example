# Generated by Django 3.2.5 on 2021-11-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='joy_profile_pic',
            field=models.ImageField(blank=True, upload_to='joyan_profile_pics'),
        ),
    ]
