from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),

    path('create/', views.create, name='create'),

    path('<int:question_id>/update/', views.update, name='update'),

    path('<int:question_id>/delete/', views.delete, name='delete'),

    path('<int:question_id>/choices/create/', views.choice_create, name='choice_create'),

    path('<int:question_id>/choices/<int:choice_id>/delete/', views.choice_delete, name='choice_delete'),
]
