# Generated by Django 3.0.8 on 2020-08-04 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_website_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=200)),
            ],
        ),
    ]
