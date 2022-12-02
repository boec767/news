from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('create/', views.CreateNews.as_view(), name='createNews'),
    path('categry/<slug:slug>/', views.HomeCategory.as_view(), name='category'),
    path('detail/<slug:slug>/', views.DetailPageView.as_view(), name='detail'),
]
