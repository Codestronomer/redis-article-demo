# Generated by Django 3.1.7 on 2022-02-21 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='item_name',
            new_name='name',
        ),
    ]
