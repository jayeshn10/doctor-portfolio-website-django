# Generated by Django 3.1.4 on 2021-01-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanager', '0012_auto_20210103_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_published',
            field=models.BooleanField(verbose_name='Publish Status'),
        ),
    ]