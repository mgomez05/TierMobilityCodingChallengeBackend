# Generated by Django 4.1.2 on 2022-10-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='shortUrl',
            field=models.CharField(max_length=200),
        ),
    ]
