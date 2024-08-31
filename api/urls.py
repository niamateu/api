from django.urls import path
from api import views

app_name = 'api'
#ルーティング情報
urlpatterns = [
    path('foods/', views.index, name='index'), #一覧
    path('foods/add/', views.edit, name='add'), #新規
    path('foods/edit/<int:id>/', views.edit, name='edit'), #編集（idを指定）
    path('foods/delete/<int:id>/', views.delete, name='delete'), #削除（idを指定）
]