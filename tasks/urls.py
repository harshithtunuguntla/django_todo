
from os import name
from django.urls import path

from . import views


urlpatterns = [
    path('',views.tasks_page,name="taskspage"),
    path('update/',views.update,name="update"),
    path('update/<int:update_id>',views.updateid,name="updateval"),
    path('delete/<int:delete_id>',views.deleteid,name="deleteval"),
    path('add/',views.add,name="add")
    ]