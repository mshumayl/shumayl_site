# Generated by Django 3.1.2 on 2021-08-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210808_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]