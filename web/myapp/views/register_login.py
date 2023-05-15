from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from ..models import MyUser
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 로그인에 성공하면 home 페이지로 이동
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


#회원 가입 폼과 뷰

class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
