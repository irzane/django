# Generated by Django 2.2.6 on 2020-10-19 10:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('material', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('imglink', models.CharField(blank=True, max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Time')),
                ('slug', models.CharField(max_length=255)),
                ('Descriptions', models.TextField(blank=True)),
                ('keyword', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
