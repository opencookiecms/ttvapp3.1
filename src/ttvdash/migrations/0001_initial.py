# Generated by Django 3.1.5 on 2021-01-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ttvproject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(blank=True, max_length=150)),
                ('p_company', models.CharField(blank=True, max_length=100)),
                ('p_code', models.CharField(blank=True, max_length=150)),
                ('p_model', models.CharField(blank=True, max_length=150)),
                ('p_desc', models.CharField(blank=True, max_length=150)),
                ('p_startdate', models.CharField(blank=True, max_length=150)),
                ('p_enddate', models.CharField(blank=True, max_length=150)),
                ('p_status', models.CharField(blank=True, max_length=150)),
                ('p_type', models.CharField(blank=True, max_length=150)),
                ('p_comp', models.CharField(blank=True, max_length=150)),
                ('p_userid', models.IntegerField(blank=True, default=0)),
                ('p_color', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
