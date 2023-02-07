
from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.urls import reverse

from . import views
from tasks.views import tasks_page,update
from django.contrib.auth import login as auth_login

from tasks.models import tasks

# Create your views here.


def create_default_tasks(user):

    new_task = tasks()
    # new_task.id=len(task_list)+1
    new_task.title = "UPCOMING FEATURES"
    new_task.description = "New features adding up soon!! 😊 Features would include filtering, creating multiple lists and so on!!"
    new_task.is_deleted=False
    new_task.completed=False
    new_task.priority = "High Priority"
    new_task.prev_priority = new_task.priority
    new_task.user = user
    new_task.username = user.username
    new_task.number=1
    # added_tasks.append(content)
    new_task.save()

    new_task = tasks()
    # new_task.id=len(task_list)+1
    new_task.title = "FEATURES"
    new_task.description = "In this do list you can add your do list items with title,description and you can also set priority to indicate the level of urgency! You can complete the task by clicking mark as done(you can undo them as well 😅). Mind to free up space? Trash it! 💯"
    new_task.is_deleted=False
    new_task.completed=False
    new_task.priority = "Medium Priority"
    new_task.prev_priority = new_task.priority
    new_task.user = user
    new_task.username = user.username
    new_task.number=1
    # added_tasks.append(content)
    new_task.save()

    new_task = tasks()
    # new_task.id=len(task_list)+1
    new_task.title = "WELCOME!!!"
    new_task.description = "This webpage is designed to have a priority based do list for improving productivity! By the way this is the description box where you can write the description for your task! 😁"
    new_task.is_deleted=False
    new_task.completed=False
    new_task.priority = "Low Priority"
    new_task.prev_priority = new_task.priority
    new_task.user = user
    new_task.username = user.username
    new_task.number=1
    # added_tasks.append(content)
    new_task.save()



def login(request):
    
    if request.method=="POST":
        username = request.POST['user_name']
        password = request.POST['password']
        
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth_login(request,user)
            print("authenticated successfully")
            # return HttpResponse("Login authenticated")
            if request.GET.get('next',None):
                print("Authenticated and redirecting to the url")
                return HttpResponseRedirect(request.GET['next'])
            else:
                return redirect('../../tasks')
                print("This guy just wanted to login, what can I return? Profile? Need to create! Till then just see logged in")
                return HttpResponse("Succeslly logged in!! No next url")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")

    else:
        return render(request,"login.html")


def signup(request):    
    if request.method=="POST":
        print("inside post")
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user_name = request.POST["user_name"]
        email_id = request.POST["email_id"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        
        if password==confirm_password:

            if User.objects.filter(username=user_name).exists():

                messages.info(request,"Username Already Exists,try again")
                return redirect("signup")
            elif User.objects.filter(email=email_id).exists():

                messages.info(request,"Email-id Already Exists")
                return redirect("signup")
            else:

                user = User.objects.create_user(username=user_name,password=password,email=email_id,first_name=first_name,last_name=last_name)
                user.save()
                create_default_tasks(user)

        else:
            messages.info(request,"Passwords Doesn't match")
            return redirect("signup")

        return redirect("login")

    else:
        print("inside else")
        return render(request,"signup.html")


def logout(request):
    auth.logout(request)
    # return HttpResponse("You have been succesfully logged out!")
    return redirect('/')

def home(request):
    return render(request,"home.html")