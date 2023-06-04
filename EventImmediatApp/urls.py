from django.urls import path
from . import views

urlpatterns =[ 
    path('', views.home, name='home'),
    path('login', views.connection, name='login'),
    path('logout', views.disconnection, name='logout'),
    path('register', views.register, name='register'),
    path('events/list', views.events_list, name='events_list'),
    path('events/create', views.events_create, name='events_create'),
    path('events/edit/<int:id>', views.events_edit, name='events_edit'),
    path('events/delete/<int:id>', views.events_delete, name='events_delete'),
    path('events/details/<int:id>', views.events_details, name='events_details'),
    path('events/join/<int:id>', views.events_join, name='events_join'),
    path('events/me', views.events_me, name='events_me'),
    path('events/cancel/<int:id>', views.events_cancel, name='events_cancel'),
    ]