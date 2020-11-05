from django.shortcuts import render
from .models import Todo
from django.utils import timezone
from django.http import  HttpResponseRedirect

# Create your views here.


def home(request):
    
    
    return render(request, 'base.html')


def add_todo(request):
    
    todo_item = request.POST.get('todo')
    add_time = timezone.now()
    
    #adding to db
    Todo.objects.create(text = todo_item,add_date = add_time)
    #get the Todo object
    todo_items = Todo.objects.all().order_by('-add_date')    
    
    stuff_for_frontend = {
        
        'todo_items' : todo_items
    }
    return render(request, 'todo/add_todo.html', stuff_for_frontend)    

def delete_todo(request, todo_id):
    
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    todo_items = Todo.objects.all().order_by('-add_date')
    
    frontend_stuff = {
        'todo_items' : todo_items
    }
    return HttpResponseRedirect('/')