from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

#create a router object #for viewsets
router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee') #take care of .as_view() and other 
                                                                         # using basename only using viewsets.ViewSet

urlpatterns = [
    path('students/' ,views.studentsView),
    path('students/<int:pk>', views.studentDetailView),
    
    #Class based view (also used for mixins and generics)
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>', views.EmployeeDetail.as_view()),
    
    path('', include(router.urls)),
    
    path('blogs/', views.BlogsView.as_view()),
    path('blogs/<int:pk>/', views.EditBlogsView.as_view()),
    
    path('comments/', views.CommentsView.as_view()),
    path('comments/<int:pk>/', views.EditCommentsView.as_view()),
]
