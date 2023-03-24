# Effi
Simple task app created with Django

## General info
An application designed to share tasks and control workload (via scoring) in small teams (around 15 members) with common goal. The idea for the application was created while working in charity organization with coordination problem.

PL Aplikacja przeznaczona do dzielenia się zadaniami i kontroli ich rozłożenia (poprzez punktację) przeznaczona dla mniejszych zespołów (do 15 członków) ze wspólnym celem. Pomysł na aplikację powstał podczas działania w organizacji charytatywnej mierzącej się z trudnościami zwiaznaymi z koordynacją.

## Technologies
- Python3, Django
- Bootsrap 4

## Features:
- task management
- list od subtasks
- comments

## To do:
- communicator
- notifications
- drafts

## Setup: 
- git clone https://github.com/annamarchewka/Effi-App.git
- cd Effi-App
- virtualenv -p python3 venv
- source venv/bin/activate
- (env) pip install django
- (env) pip install psycopg2
- (env) pip install -r requirements.txt
- (env) python manage.py migrate
- (env) python manage.py runserver
