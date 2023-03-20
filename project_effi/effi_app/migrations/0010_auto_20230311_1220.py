# Generated by Django 3.2.18 on 2023-03-11 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('effi_app', '0009_auto_20230311_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='task',
            name='podtask',
        ),
        migrations.RemoveField(
            model_name='task',
            name='username',
        ),
        migrations.AddField(
            model_name='task',
            name='username',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='effi_app.user_info'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User_infoTask',
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='effi_app.task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='effi_app.task'),
        ),
    ]