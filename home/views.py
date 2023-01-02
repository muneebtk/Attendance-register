from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Attendance, Employee
from rest_framework import status
from django .shortcuts import get_object_or_404
from datetime import datetime


# checkin an employee
@api_view(['POST'])
def Checkin(request):
    empId = request.POST['emp_id']
    employee = get_object_or_404(Employee,emp_id=empId)
    Attendance.objects.create(
        employee = employee,
        attended = True
    )
    return Response({'data':'you were checkined'},status=status.HTTP_200_OK)

# checkout a employee
@api_view(['POST'])
def Chekcout(request):
    emp_id=request.POST['emp_id']
    today = datetime.now().date()
    current_time = datetime.utcnow()
    employee = get_object_or_404(Employee,emp_id=emp_id)
    emp=Attendance.objects.filter(employee__emp_id=emp_id).first()
    if Attendance.objects.filter(employee=employee,attended=True).exists() and emp.checkin.date()==today:
        checkout_time = Attendance.objects.filter(employee=employee).first()
        x = Attendance.objects.order_by('-checkin').filter(employee=employee).first()
        if x.checkin.date()==today:
            a=str(x.checkin.time()).split('.')[:1]
            b=str(current_time.time()).split('.')[:1]
            c=''.join(i for i in a)
            d=''.join(i for i in b)
            t1 = datetime.strptime(c, "%H:%M:%S")
            t2 = datetime.strptime(d, "%H:%M:%S")
            delta=t2-t1
            checkout_time.available_time=delta.total_seconds()/(60*60)
        checkout_time.checkout = datetime.now()
        checkout_time.save()
        
        return Response({'message':'checkout success.!'})
    else:
        return Response({'message':'You are not checkined.!'})

# find the employee is attended or not and is attended return the time duration
@api_view(['POST'])
def get_attendance_report(request):
    employee_id = request.POST['emp_id']
    date = request.POST['date']
    try:
        x = Attendance.objects.filter(employee__emp_id=employee_id,checkin__contains=date).first()
        attended=x.attended
        available_time = x.available_time
        context={
            'attended':attended,
            'availabel_time':f'{available_time} hours',
        }
        return Response(context,status=status.HTTP_200_OK)
    except:
        return Response({'message':'There is no attendance data found!'})
        
    

