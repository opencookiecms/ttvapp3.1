# Generated by Django 3.1.5 on 2021-01-06 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttvdash', '0004_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageOfTheday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlemessage', models.CharField(blank=True, max_length=50)),
                ('MessageOfTheday', models.CharField(blank=True, max_length=250)),
                ('postby', models.CharField(blank=True, max_length=50)),
                ('timepost', models.CharField(blank=True, max_length=10)),
                ('postimages', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
