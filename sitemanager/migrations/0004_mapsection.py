# Generated by Django 3.1.4 on 2021-01-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanager', '0003_auto_20201231_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_title', models.CharField(max_length=255, verbose_name='Title')),
                ('address', models.TextField(verbose_name='Caption')),
                ('address_url', models.URLField(verbose_name='Image')),
                ('avl_time', models.CharField(max_length=255, verbose_name='Image')),
                ('contact_no', models.CharField(max_length=255, verbose_name='Image')),
            ],
            options={
                'verbose_name_plural': 'Map Section',
            },
        ),
    ]
