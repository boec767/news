from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, FormView, CreateView
from .form import NewUserForm

from .models import NewsBlog, Category


class HomePageView(ListView):
    template_name = 'main/main_home.html'
    model = NewsBlog
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categorys'] = Category.objects.all()
        return context


class HomeCategory(HomePageView):

    def get(self, request, **kwargs):
        slug = kwargs.get('slug')
        self.queryset = NewsBlog.objects.filter(category__slug=slug)
        return super().get(request, **kwargs)


class DetailPageView(DetailView):
    template_name = 'main/main_detail.html'
    model = NewsBlog
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = NewsBlog.objects.all()
        context['categorys'] = Category.objects.all()
        return context


class CreateNews(CreateView):
    model = NewsBlog
    fields = ['title', 'category', 'user', 'img', 'content', ]
    template_name = 'main/main_create_news.html'
    success_url = reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = NewsBlog.objects.all()
        context['categorys'] = Category.objects.all()
        return context
