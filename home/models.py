from django.db import models

# employee table 
class Employee(models.Model):
    emp_id = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    job = models.CharField(max_length=300)
    def __str__(self):
        return self.email

# attendance table
class Attendance(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(null=True)
    attended = models.BooleanField(default=False)
    available_time= models.DateTimeField(null=True)
    
    def __str__(self):
        return self.employee.name