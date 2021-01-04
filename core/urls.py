from django.urls import path
from core import views

app_name='core'
urlpatterns=[
    path('', views.home, name='home'),
    #path('', views.alvos_list, name='list_alvos'),
    path('alvo_create/', views.alvo_create, name='alvo_create'),
    path('alvo_update/<int:pk>', views.alvo_update, name='alvo_update'),
    path('alvo_delete/<int:pk>', views.alvo_delete, name='alvo_delete'),
]