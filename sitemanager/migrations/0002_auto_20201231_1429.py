# Generated by Django 3.1.4 on 2020-12-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_img',
            field=models.ImageField(upload_to='blogimages/'),
        ),
    ]
