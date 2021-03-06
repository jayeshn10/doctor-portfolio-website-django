# Generated by Django 3.1.4 on 2021-01-03 14:07

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanager', '0011_blogs_blog_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_pubdate',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, verbose_name='Published Date & Time'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='blog_published',
            field=models.BooleanField(verbose_name='Published Status'),
        ),
    ]
