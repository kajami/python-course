from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class BookListView(ListView):
    model = models.Book

class BookDetailView(DetailView):
    model = models.Book

class BookUpdateView(UpdateView):
    model = models.Book
    fields = [
        'name',
        'author',
        'year',
        'image',
        'username',
        'addingDate',
    ]
    success_url ='/books/'

class BookDeleteView(DeleteView):
    model = models.Book
    success_url ='/books/'

class BookCreateView(CreateView):
    model = models.Book
    template_name = 'bookCollectionApp/book_create.html'
    fields = [
        'name',
        'author',
        'year',
        'image',
        'username',
        'addingDate',
    ]
    success_url ='/books/'

#if user makes POST request on login.html, try authenticate. If user is found redirect to /books/.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login successful."))
            return redirect('/books/')
        else:
            messages.error(request, ("Login error, try again."))
            return redirect('/')
    else:
        return render(request, 'bookCollectionApp/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out."))
    return redirect('/')

#if user makes POST request on register_user.html, program tries to create a new user with UserCreationForm, else it will only render UserCreationForm in page.
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful!"))
            return redirect('/books/')
    else:
        form = UserCreationForm()
    return render(request, 'bookCollectionApp/register_user.html', {'form': form,})