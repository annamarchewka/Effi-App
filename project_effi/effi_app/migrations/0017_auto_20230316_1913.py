# Generated by Django 3.2.18 on 2023-03-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('effi_app', '0016_comment_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='task',
            new_name='task_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Presence',
        ),
    ]