# todo/views.py
from django.shortcuts import render, redirect
from.models import TodoItem
from.forms import TodoItemForm

def todo_list(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todo_items': todo_items})

def create_todo_item(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm()
    return render(request, 'todo/create_todo_item.html', {'form': form})

def update_todo_item(request, pk):
    todo_item = TodoItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=todo_item)
    return render(request, 'todo/update_todo_item.html', {'form': form})

def delete_todo_item(request, pk):
    TodoItem.objects.get(pk=pk).delete()
    return redirect('todo_list')