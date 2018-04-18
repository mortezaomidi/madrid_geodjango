# Generated by Django 2.0.1 on 2018-02-12 22:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrid', '0002_delete_fine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=10)),
                ('address', models.TextField(max_length=100)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('timestamp', models.TextField(max_length=8)),
                ('tax', models.FloatField()),
                ('discount', models.BooleanField()),
                ('points', models.IntegerField()),
                ('informer', models.TextField(max_length=50)),
                ('fact', models.TextField(max_length=500)),
                ('speed_limit', models.FloatField(null=True)),
                ('speed_reg', models.FloatField(null=True)),
                ('geocoder_info', models.TextField(max_length=1000)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]