# Generated by Django 4.1.7 on 2023-04-03 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mari_efficiency', '0002_rename_items_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
    ]
