from django.urls import path
from . import views

urlpatterns = [
    path('students/' ,views.studentsView),
    path('students/<int:pk>', views.studentDetailView),
    
    #Class based view
    path('employees/', views.Employees.as_view()),
]
