from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentList, name='student-list'),
    path('student/<int:pk>/', views.StudentView, name='student-view'),
    path('student/create/', views.StudentCreate, name='student-create'),
    path('student/update/<int:pk>/', views.StudentUpdate, name='student-update'),
    path('student/delete/<int:pk>/', views.StudentDelete, name='student-delete'),

    path('students-list-create/', views.StudentListCreate, name='student-list-create'),
    path('student-detail/<int:pk>/', views.StudentDetail, name='student-detail'),
]