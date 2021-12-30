from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpRequest
# Create your views here.

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import tasks




# task1 = tasks()
# task1.id=1
# task1.title = "TESTING TASK 1"
# task1.completed=True
# task1.is_deleted=False
# task1.priority=1
# task1.description="testing task with high priority"
# task1.prev_priority=1

# task2 = tasks()
# task2.id=2
# task2.title = "TESTING TASK 2"
# task2.description = "testing task with low priority"
# task2.completed=False
# task2.is_deleted=False
# task2.priority=3
# task2.prev_priority=3


# task_list = [task1,task2]

added_tasks=["hello"]

@login_required()
def tasks_page(request):
    task_list = tasks.objects.filter(username=request.user).order_by('-id')
    # task_list = tasks.objects.all().order_by('-id')
    return render(request,"tasks_page_new.html",{"task_list":task_list,"added_tasks":added_tasks})

def update(request):
    return HttpResponse("Hello im in update")

def updateid(request,update_id):
    task = tasks.objects.get(id=update_id)
    status = task.priority

    # print(status)

    if status=="High Priority" or status=="Medium Priority" or status=="Low Priority":
        task.priority = 'Deactivated'
        task.save()
        # task_list[update_id].priority= "Deactivated"
    else:
        task.priority = task.prev_priority
        task.save()
        # task_list[update_id].priority= task_list[update_id].prev_priority


    # if update_id==1:
    #     task1.completed = not task1.completed
    # elif update_id == 2:
    #     task2.completed = not task2.completed
    return redirect(request.META.get('HTTP_REFERER'))
    # return render(request,"tasks_page.html",{"task_list":task_list,"added_tasks":added_tasks})

def deleteid(request,delete_id):
    task = tasks.objects.get(id=delete_id)
    task.is_deleted = not task.is_deleted
    task.save()

    # task_list[delete_id-1].is_deleted=True
    # if delete_id==1:
    #     task1.is_deleted=True
    # elif delete_id==2:
    #     task2.is_deleted=True
    return redirect(request.META.get('HTTP_REFERER'))
    # return render(request,"tasks_page.html",{"task_list":task_list,"added_tasks":added_tasks})


def add(request):
    task_list = tasks.objects.all()

    if request.method=="POST":
        task_title = request.POST['task_title']
        task_description = request.POST['task_description']
        task_priority = request.POST['task_priority']

        print("hello")
        print(request.user)
        


        new_task = tasks()
        # new_task.id=len(task_list)+1
        new_task.title = task_title.upper()
        new_task.description = task_description
        new_task.is_deleted=False
        new_task.completed=False
        new_task.priority = task_priority
        new_task.prev_priority = new_task.priority
        new_task.user = request.user
        new_task.username = request.user.username
        new_task.number=1
        # added_tasks.append(content)

        new_task.save()
        # task_list.append(new_task)

        # print(content)
        # print(task_list)

        # for task in task_list:
        #     if(task.priority=="High Priority"):
        #         print(1)
        #     elif(task.priority=="Low Priority"):
            
    return redirect(request.META.get('HTTP_REFERER'))
    # return render(request,"tasks_page.html",{"task_list":task_list,"added_tasks":added_tasks})
