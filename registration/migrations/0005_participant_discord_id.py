# Generated by Django 5.0 on 2023-12-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_rename_additional_comments_participant_motivation'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='discord_id',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
