from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/<int:event_id>', views.event, name='event'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.sign_out, name='logout')
]


