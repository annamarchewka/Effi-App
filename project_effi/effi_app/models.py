from django.db import models

CITIES = [
    (1, 'Warszawa'),
    (2, 'Poznań'),
    (3, 'Gdańsk'),
    (4, 'Katowice'),
    (5, 'Kraków'),
]

ROLES = [
    (1, 'Ativist'),
    (2, 'Coordinator'),
]

POINTS = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
]

MODES = [
    (1, 'remotely'),
    (2, 'based in city'),
]

class Group(models.Model):
    group_name = models.CharField(max_length=64, null=False)
    city = models.IntegerField(choices=CITIES, default=1)
    members_amount = models.IntegerField(null=True)

class User(models.Model):
    name_surname = models.CharField(max_length=64, null=False)
    nickname = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, default='hello_effi123!')

class User_info(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE)
    mode = models.IntegerField(choices=MODES, default=2)

class Task(models.Model):
    task_name = models.CharField(max_length=64, null=False)
    task_descr = models.CharField(max_length=64, null=True)
    estimated_time = models.IntegerField(null=True)
    points = models.IntegerField(choices=POINTS, default=1)
    nickname = models.ManyToManyField(User_info, through='User_infoTask')

class User_infoTask(models.Model):
    nickname = models.ForeignKey(User_info, on_delete=models.CASCADE)
    task_name = models.ForeignKey(Task, on_delete=models.CASCADE)
    owner_amount = models.IntegerField(null=True)

class Presence(models.Model):
    name_surname = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
    presence = models.BooleanField(null=False)

