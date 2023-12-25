from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, SignInForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)

            # Сохранение данных в файл (users.txt)
            with open('users.txt', 'a') as file:
                file.write(f'Username: {user.username}, Email: {user.email}, Password: {user.password}\n')

            return redirect('user_profile', username=user.username)

    else:
        form = SignUpForm()

    return render(request, 'main/signup.html', {'form': form})

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # Создание пользователя, но не сохранение в базу данных
#             user = form.save(commit=False)
#
#             # Сохранение данных в файл (users.txt)
#             with open('users.txt', 'a') as file:
#                 file.write(f'Username: {user.username}, Email: {user.email}, Password: {user.password}\n')
#
#             # Сохранение пользователя в базу данных
#             user.save()
#
#             # Аутентификация пользователя
#             login(request, user)
#
#             # Перенаправление на другую страницу
#             return redirect('user_profile', username=user.username)
#
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'main/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homeShop1')
    else:
        form = SignInForm()
    return render(request, 'main/signin.html', {'form': form})



def homeShop(request):
    news = Articles.objects.all()
    # news = Articles.objects.all()[:1]
    # выбрать только 1 запись
    # news = Articles.objects.order_by('title')
    # сортировка по уменьшению числа и по алфавиту от а до я
    # news = Articles.objects.order_by('-title')
    # сортировка по увеличению числа и по алфавиту от я до а
    return render(request, 'main/homeShop1.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeShop1')
        else:
            error = "Форма неверна!"

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)

def index(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def info(request):
    return render(request, 'main/info.html')

def write_to_file(request):
    content = "Запис у файл"

    # Открываем файл для записи ('w' означает запись)
    with open('example.txt', 'w') as file:
        file.write(content)

    return HttpResponse("Запись в файл выполнена успешно.")

def read_from_file(request):
    try:
        # Открываем файл для чтения ('r' означает чтение)
        with open('example.txt', 'r') as file:
            content = file.read()
            return HttpResponse(f"Вміст файлу: {content}")
    except FileNotFoundError:
        return HttpResponse("Файла не найдено!")


def user_profile(request, username):
    user_data = []

    # Чтение всех строк из файла
    with open('users.txt', 'r') as file:
        for line in file:
            user_data.append(line.strip())

    return render(request, 'main/user_profile.html', {'user_data': user_data})