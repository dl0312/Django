# Generated by Django 2.0.1 on 2018-01-28 18:46

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180129_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=blog.models.upload_location, width_field='width_field'),
        ),
    ]