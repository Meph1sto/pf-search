# Generated by Django 2.0.2 on 2018-03-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KISCOURSEID', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('TITLE', models.CharField(max_length=100)),
                ('UNI_NAME', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
