# Generated by Django 5.0 on 2023-12-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
