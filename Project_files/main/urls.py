from django.urls import path
from . import views
from .views import homeShop, create, signup, signin, user_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homeShop, name='homeShop1'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
    path('create/', views.create, name='create'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='homeShop1'), name='logout')

]
