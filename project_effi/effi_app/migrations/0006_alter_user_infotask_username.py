# Generated by Django 3.2.18 on 2023-03-10 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('effi_app', '0005_remove_user_infotask_owner_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_infotask',
            name='username',
            field=models.ForeignKey(default='no owner', on_delete=django.db.models.deletion.CASCADE, to='effi_app.user_info'),
        ),
    ]