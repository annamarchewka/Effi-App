"""project_effi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from effi_app.views import LoginFormView, MainView, TaskView, TaskDetailView, AddTaskView, ProfileView, logout_view, change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginFormView.as_view(), name='login'),
    path('accounts/profile/', MainView.as_view(), name="main"),
    path('tasks/<int:usernameid>/', TaskView.as_view(), name="tasks"),
    path('taskdetail/<int:id>/', TaskDetailView.as_view(), name="taskdetail"),
    path('addtask/<int:usernameid>/', AddTaskView.as_view(), name="addtask"),
    path('profile/<int:usernameid>/', ProfileView.as_view(), name="profile"),
    path('logout', logout_view, name='logout'),
    path('change-password/', change_password, name='change_password'),
]
