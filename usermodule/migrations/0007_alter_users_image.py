# Generated by Django 4.2.7 on 2024-04-26 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0006_alter_users_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
