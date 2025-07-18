from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer
from .paginations import CustomPagination
from employees.filters import EmployeeFilter
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



# function based view for student
@api_view(['GET','POST'])
def studentsView(request):
  #Mannual serializer
  # students = Student.objects.all()
  # students_list = list(students.values())
  # return JsonResponse(students_list, safe=False)
  
  if request.method == 'GET':
    #Get all the data from Student table
    students = Student.objects.all()
    serializer = StudentSerializer(students, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentDetailView(request, pk):
  try:
    student = Student.objects.get(pk=pk)
  except Student.DoesNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = StudentSerializer(student)
    return Response(serializer.data, status = status.HTTP_200_OK)
  
  elif request.method == 'PUT':
     serializer = StudentSerializer(student, data = request.data)
     if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
     else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#Class based view for Employees 
# class Employees(APIView):
  # def get(self, request):
  #   employees = Employee.objects.all()
#     serializer = EmployeeSerializer(employees, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
  
#   def post(self, request):
#     serializer = EmployeeSerializer(data = request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status = status.HTTP_201_CREATED)
#     return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
  
# class EmployeeDetail(APIView):
#   def get_object(self, pk):
#     try:
#       return Employee.objects.get(pk=pk)
#     except Employee.DoesNotExist:
#       raise Http404
  
#   def get(self, request, pk):
#     employee = self.get_object(pk)
#     serializer = EmployeeSerializer(employee)
#     return Response(serializer.data, status = status.HTTP_200_OK)
  
#   def put(self, request, pk):
#     employee = self.get_object(pk)
#     serializer = EmployeeSerializer(employee, data = request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  
#   def patch(self, request, pk):
#     employee = self.get_object(pk)
#     serializer = EmployeeSerializer(employee, data = request.data, partial = True)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  
#   def delete(self, request, pk):
#     employee = self.get_object(pk)
#     employee.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
 
"""
# Using mixins and GenericAPIView   
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  
  def get(self, request):
    return self.list(request)
  
  def put(self, request):
    return self.create(request)

class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  
  def get(self, request, pk):
    return self.retrieve(request,pk)
  
  def put(self, request, pk):
    return self.update(request, pk)
  
  def delete(self, request, pk):
    return self.destroy(request, pk)
  """
  
  

"""
#Generics
class Employees(generics.ListCreateAPIView):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer
   
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  lookup_field = 'pk'
  """
  
#using viewsets.ViewSet
"""
class EmployeeViewset(viewsets.ViewSet):
  
  
  def list(self, request):
    queryset = Employee.objects.all()
    serializer = EmployeeSerializer(queryset, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def create(self, request):
    serializer = EmployeeSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def retrieve(self, request, pk):
    queryset = get_object_or_404(Employee,pk = pk)
    serializer = EmployeeSerializer(queryset);
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def update(self, request, pk):
    queryset = get_object_or_404(Employee,pk = pk)
    serializer = EmployeeSerializer(queryset, data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
  
  def delete(self, request, pk):
    queryset = get_object_or_404(Employee, pk = pk)
    queryset.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    """
    
#using viewsets.ModelViewset
class EmployeeViewset(viewsets.ModelViewSet):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  pagination_class= CustomPagination
  filterset_class = EmployeeFilter              #Custom view filter
  # filter_backends = [DjangoFilterBackend]     # Required if not used in settings.py
  # filterset_fields = ['designation']            #Global Filter
  
  
  
  
# Blog views using generics
class BlogsView(generics.ListCreateAPIView):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['blog_title','blog_body']
  ordering_fields = ['id']
  
  
class EditBlogsView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer
  lookup_field = 'pk'
  
class CommentsView(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  
class EditCommentsView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  lookup_field = 'pk'
