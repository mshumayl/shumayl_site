# Generated by Django 3.1.2 on 2021-08-07 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210808_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.TextField(default='EmptyText', max_length=500),
        ),
    ]
