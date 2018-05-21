from django.shortcuts import render, redirect
# Importing user creation form for new user registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Importing Todo model
from .models import Todo
from .forms import TodoForm


# View for index page
def index(request):
    if request.user.is_authenticated:
        # This is filtering only current user's todos
        todos = Todo.objects.filter(user=request.user)[:]

        context = {
            'todos' : todos
        }

        # Returning index.html and context in it
        return render(request, 'todos/index.html', context)
    else:
        return render(request, 'todos/home.html')


# View for single todo
@login_required
def details(request, id):
    single_todo = Todo.objects.get(id=id)
    context = {
        'todo_details' : single_todo
    }
    return render(request, 'todos/details.html', context)


# View for Add form
@login_required
def add(request):
    form = TodoForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/todos')

    else:
        return render(request, 'todos/add.html', {'form' : form})


# View for Edit form
@login_required
def edit(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/todos')

    else:
        return render(request, 'todos/add.html', {'form' : form, 'todo' : todo})


# View for Delete todo
@login_required
def delete(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == 'POST':
        todo.delete()
        return redirect('/todos')

    else:
        return render(request, 'todos/delete-confirm.html', {'todo' : todo})
        

# View for Signup form
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username= username, password= password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {
        'form' : form
    }
    return render(request, 'registration/signup.html', context)

