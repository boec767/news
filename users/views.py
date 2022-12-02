from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render, redirect

from main.form import NewUserForm
from main.models import NewsBlog, Category
from users.forms import UserCreationForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class LoginUser(PasswordChangeView, Register):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = NewsBlog.objects.all()
        context['categorys'] = Category.objects.all()
        return context


class RegisterNewUser(CreateView):
    template_name = 'registration/create_user.html'
    form_class = NewUserForm
    success_url = reverse_lazy('login')
