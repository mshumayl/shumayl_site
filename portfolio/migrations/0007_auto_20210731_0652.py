# Generated by Django 3.1.2 on 2021-07-30 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_remove_post_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_datetime',
            new_name='post_date',
        ),
    ]