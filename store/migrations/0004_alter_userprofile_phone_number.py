# Generated by Django 5.1.3 on 2024-11-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_userprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.PositiveIntegerField(default='Not provided', max_length=15),
        ),
    ]