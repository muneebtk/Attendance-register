from django.urls import path
from . import views
urlpatterns = [
    path('checkin/',views.Checkin),
    path('checkout/',views.Chekcout),
    path('find_attendance/',views.get_attendance_report),


]