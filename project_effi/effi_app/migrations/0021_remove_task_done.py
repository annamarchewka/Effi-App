# Generated by Django 3.2.18 on 2023-03-17 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('effi_app', '0020_remove_group_members_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='done',
        ),
    ]
