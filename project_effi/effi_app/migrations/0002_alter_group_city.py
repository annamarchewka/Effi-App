# Generated by Django 3.2.18 on 2023-02-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('effi_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='city',
            field=models.IntegerField(choices=[(1, 'Warszawa'), (2, 'Prague'), (3, 'Bratislava')], default=1),
        ),
    ]
