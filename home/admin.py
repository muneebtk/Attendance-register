from django.contrib import admin
from . models import Employee, Attendance

# class AttendanceAdmin(admin,)
# admin.site.register(Employee)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id','email')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('checkin','checkout')