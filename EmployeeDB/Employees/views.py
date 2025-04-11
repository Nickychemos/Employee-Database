from django.shortcuts import render
from .serializers import EmployeeSerializer, BranchSerializer, ManagerSerializer
from .models import Employee, Branch, Manager
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

#Employee views
@api_view(['GET', 'POST'])

def employee_list(request, format = None):

    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':

        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Error':'Data not valid'},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def employee_details(request, id, format = None):

    try:
        details = Employee.objects.get(id = id)
    except details.DoesNotExist:
        return Response({"Error":"Employee details not found"}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = EmployeeSerializer(details)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    
    elif request.method == 'PUT':

        serializer = EmployeeSerializer(details, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':

        details.delete()
        return Response({"Success": "Item deleted successfully"})


#Manager Views
@api_view(['GET', 'POST'])

def manager_list(request, format = None):

    if request.method == 'GET':
        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    elif request.method == 'POST':

        serializer = ManagerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def manager_details(request, id, format = None):
    
    try:
        details = Manager.objects.get(id = id)
    except details.DoesNotExist:
        return Response("Manager does not exist", status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':

        serializer = ManagerSerializer(details)
        return Response(serializer.data)
    
    elif request.method == 'PUT':

        serializer = ManagerSerializer(details)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        details.delete()
        return Response("Item successfully deteled", status=status.HTTP_204_NO_CONTENT)
    

#Branch Views
@api_view(['GET', 'POST'])

def branch_list(request, format = None):

    if request.method == 'GET':

        details = Branch.objects.all()
        serializer = BranchSerializer(details, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':

        serializer = BranchSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])

def branch_details(request, id, format = None):

    try:
        details = Branch.objects.get(id = id)
    except details.DoesNotExist:
        return Response("Branch not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = BranchSerializer(details)
        return Response(serializer.data)
    
    elif request.method == 'PUT':

        serializer = BranchSerializer(details, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
#View to get employees working in the 3 branches

@api_view(['GET'])
def Kisumu_list(request, branch):
    try:
        kisumu_branch = Branch.objects.get(branch_name=branch)
    except Branch.DoesNotExist:
        return Response({"error": "Branch not found"}, status=status.HTTP_404_NOT_FOUND)
    employees = Employee.objects.filter(branch = kisumu_branch)
    serializer = EmployeeSerializer(employees, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def Nairobi_list(request, branch):

    try:
        Nairobi_branch = Branch.objects.get(branch_name = branch)
    except Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    employees = Employee.objects.filter(branch = Nairobi_branch)
    serializer = EmployeeSerializer(employees)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Mombasa_list(request, branch):
    try:
        mombasa_branch = Branch.objects.get(branch_name = branch)
    except Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    mombasa_employees = Employee.objects.filter(branch = mombasa_branch)
    serializer = EmployeeSerializer(mombasa_employees)
    return Response(serializer.data, status=status.HTTP_200_OK)


