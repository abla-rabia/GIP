# Generated by Django 5.0 on 2023-12-17 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_remove_participant_address_remove_participant_role_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='additional_comments',
            new_name='motivation',
        ),
    ]