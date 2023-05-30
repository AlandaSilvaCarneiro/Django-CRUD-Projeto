from cliente import views
from django.urls import path

app_name = "cliente"
urlpatterns = [
    path('', views.ClienteList.as_view(),name='list'),
    path('create/',views.ClienteCreate.as_view(),name='create'),
    path('update/<int:pk>/',views.ClienteUpdate.as_view(),name='update')
]
