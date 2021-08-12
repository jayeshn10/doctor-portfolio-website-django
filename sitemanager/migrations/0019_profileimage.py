# Generated by Django 3.1.4 on 2021-01-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanager', '0018_blogextraimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_caption', models.CharField(max_length=255, verbose_name='Caption')),
                ('image_src', models.ImageField(upload_to='Profileimage/', verbose_name='Image')),
            ],
            options={
                'verbose_name_plural': 'Profile Image',
            },
        ),
    ]