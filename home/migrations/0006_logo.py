# Generated by Django 2.2.6 on 2020-10-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201020_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('logo', models.CharField(max_length=200)),
            ],
        ),
    ]
