# Generated by Django 3.2.9 on 2022-02-04 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websurat', '0005_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='pdf',
            field=models.FileField(upload_to='static/doc/'),
        ),
    ]