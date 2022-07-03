# Generated by Django 2.2.6 on 2020-10-19 10:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration): 

    dependencies = [
        ('home', '0002_auto_20201019_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Content_Heading',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='About_Content_Paragraph',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='About_Content_Top_Down',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='About_Three_Content',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='LatestProducts_Content',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VideoSection',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('video_link', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AddField(
            model_name='popularproducts',
            name='Descriptions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='popularproducts',
            name='keyword',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='popularproducts',
            name='slug',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='popularproducts',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Time'),
        ),
    ]
