# Generated by Django 5.0.2 on 2024-02-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_permission_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='created_At',
            field=models.DateField(auto_now=True),
        ),
    ]