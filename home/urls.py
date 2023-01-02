from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('checkin/',views.Checkin),
    path('checkout/',views.Chekcout),

]