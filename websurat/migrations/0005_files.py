# Generated by Django 3.2.9 on 2022-02-03 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websurat', '0004_auto_20211130_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='store/doc/')),
            ],
        ),
    ]
