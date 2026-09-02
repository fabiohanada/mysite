from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o usuário no banco de dados
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has benn successfully created')
            return redirect('myapp:index')  # Redireciona para a página principal ou login
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form': form})
