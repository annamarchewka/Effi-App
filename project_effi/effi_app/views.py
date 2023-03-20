from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User_info, Group, Task, Subtask, Comment
from .forms import SubtaskForm, CommentForm, AddForm, DeleteForm
class LoginFormView(LoginView):
    template_name = 'login.html'
    success_url = 'main/'
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return redirect('login')
def logout_view(request):
    logout(request)
    return redirect('login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

class MainView(View):
    def get(self, request):
        user = request.user
        profile = User_info.objects.get(pk=user)
        members = User_info.objects.all()
        gn = profile.group_name
        g = gn.group_name
        return render(request, "main.html", {"members": members, "group_name": g})

class TaskView(View):
    def get(self, request, usernameid):
        mytasks = Task.objects.filter(username_id=usernameid).filter(done=1)
        freetasks = Task.objects.filter(username_id__isnull=True).filter(done=1)
        takentasks = Task.objects.filter(username_id__gt=usernameid).filter(username_id__gte=usernameid).filter(done=1)
        return render(request, 'tasks.html', {'mytasks': mytasks, 'freetasks': freetasks, 'takentasks': takentasks})
    def post(self, request, usernameid):
        if 'task_id' in request.POST:
            task_id = request.POST.get('task_id')
            task = Task.objects.get(pk=task_id)
            task.username_id = usernameid
            task.save()
            return redirect("tasks", usernameid=usernameid)
        elif 'mytask_id' in request.POST:
            mytask_id = request.POST.get('mytask_id')
            mytask = Task.objects.get(pk=mytask_id)
            mytask.username_id = None
            mytask.save()
            return redirect("tasks", usernameid=usernameid)
        elif 'othertask_id' in request.POST:
            othertask_id = request.POST.get('othertask_id')
            othertask = Task.objects.get(pk=othertask_id)
            a = othertask.username_id
            return redirect("profile", usernameid=a)
        elif 'done_id' in request.POST:
            done_id = request.POST.get('done_id')
            donetask = Task.objects.get(pk=done_id)
            donetask.done = 0
            donetask.save()
            user = donetask.username_id
            return redirect("tasks", usernameid=user)


class TaskDetailView(View):
    def get(self, request, id):
        task = Task.objects.get(pk=id)
        subtask = Subtask.objects.filter(task_id=id)
        form = SubtaskForm()
        comments = Comment.objects.filter(task_name_id=id)
        sec_form = CommentForm()
        return render(request, 'taskdetail.html', {'task': task, 'subtask': subtask, 'form': form, 'comments': comments, 'sec_form': sec_form})
    def post(self, request, id):
        if 'first' in request.POST:
            form = SubtaskForm(request.POST)
            if form.is_valid():
                newsubtask = form.cleaned_data['subtask']
                new = Subtask.objects.create(task_id=id, subtask=newsubtask)
                return redirect("taskdetail", id=id)
            else:
                HttpResponse("Incorrect value!")
            return redirect("taskdetail", id=id)
        elif 'delsubtask' in request.POST:
            delsubtask = request.POST.get('delsubtask')
            subtodel = Subtask.objects.filter(pk=delsubtask)
            subtodel.delete()
            return redirect("taskdetail", id=id)
        elif 'deltask' in request.POST:
            deltask = request.POST.get('deltask')
            deletet = Task.objects.filter(pk=deltask)
            deletet.delete()
            user = request.user.id
            return redirect("tasks", usernameid=user)
        elif 'com' in request.POST:
            sec_form = CommentForm(request.POST)
            if sec_form.is_valid():
                newcom = sec_form.cleaned_data['content']
                newc = Comment.objects.create(task_name_id=id, username=request.user, content=newcom)
                return redirect("taskdetail", id=id)
            else:
                HttpResponse("Incorrect value!")
        elif 'delcom' in request.POST:
            delcom = request.POST.get('delcom')
            delc = Comment.objects.filter(pk=delcom)
            delc.delete()
            user = request.user.id
            return redirect("taskdetail", id=id)


class AddTaskView(View):
    def get(self, request, usernameid):
        all = Task.objects.all()
        form = AddForm()
        second_form = DeleteForm()
        return render(request, 'addtask_form.html', {"form": form, 'all': all})
    def post(self, request, usernameid):
        if 'addtask' in request.POST:
            form = AddForm(request.POST)
            if form.is_valid():
                task_name = form.cleaned_data['task_name']
                task_descr = form.cleaned_data['task_descr']
                task_longdescr = form.cleaned_data['task_longdescr']
                estimated_time = form.cleaned_data['estimated_time']
                points = form.cleaned_data['points']
                status = form.cleaned_data['status']
                new = Task.objects.create(task_name=task_name, task_descr=task_descr, estimated_time=estimated_time, points=points, group_name_id=1, status=status, task_longdescr=task_longdescr)
                return redirect("tasks", usernameid=usernameid)
            else:
                return HttpResponse("Incorrect values. Check again")

class ProfileView(View):
 def get(self, request, usernameid):
     profile = User_info.objects.get(pk=usernameid)
     tasks = Task.objects.filter(username_id=usernameid).filter(done=1)
     histtasks = Task.objects.filter(username_id=usernameid).filter(done=0)
     p = []
     for i in tasks:
         point = i.points
         p.append(point)
     score = sum(p)
     profile.score = score
     return render(request, 'profile.html', {'profile': profile, 'tasks': tasks, 'score': score, 'histtasks': histtasks})


'''class ScoreView(View):
    def get(self, request):
        users = User_info.objects.all()
        task_point = Task.objects.filter(done=1)
        all_points = []
        for i in task_point:
            p = i.points
            all_points.append(p)
    return render(request, 'score.html', {'users': users})
    def post(self, request):
        pass
'''