# Generated by Django 4.2.11 on 2024-05-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_by',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
