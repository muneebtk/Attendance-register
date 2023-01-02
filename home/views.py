from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Attendance, Employee
from rest_framework import status
from django .shortcuts import get_object_or_404

@api_view(['GET'])
def home(request):
    return Response('hello world')

@api_view(['POST'])
def Checkin(request):
    empId = request.POST['emp_id']
    employee = get_object_or_404(Employee,emp_id=empId)
    Attendance.objects.create(
        employee = employee,
        attended = True
    )
    return Response({'data':'you were checkined'},status=status.HTTP_200_OK)

import datetime
@api_view(['POST'])
def Chekcout(request):
    emp_id=request.POST['emp_id']
    today = datetime.date.today()
    print(today,'--------------')
    employee = get_object_or_404(Employee,emp_id=emp_id)
    emp=get_object_or_404(Attendance,employee=employee)
    print(emp.checkin.date(),'=====================')
    if Attendance.objects.filter(employee=employee,attended=True).exists() and emp.checkin.date()==today:
        checkout_time = Attendance.objects.get(employee=employee)
        checkout_time.checkout = datetime.datetime.now()
        
        checkout_time.save()
        return Response({'message':'checkout success.!'})
    else:
        return Response({'message':'You are not checkined.!'})
    

