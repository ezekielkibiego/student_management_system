from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_student/', views.student_create, name='add_student'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    path('<int:pk>/edit/', views.student_update, name='student_update'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
]
