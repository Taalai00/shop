# Generated by Django 5.1.3 on 2024-11-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_userprofile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.PositiveIntegerField(max_length=15),
        ),
    ]