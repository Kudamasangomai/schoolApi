from unicodedata import name
from django.urls import path
from  . import views

from rest_framework.authtoken.views  import obtain_auth_token
urlpatterns = [

    #creating its own app is better
    path('register_user/',views.register_user),


    #login user
    path('login/',obtain_auth_token,name="login"),
    
    path('students/',views.get_students,name="students"),
    path('students/<int:pk>/',views.get_detailed_student,name="student-detail"),
    path('student_create/',views.student_create),
    path('student_delete/<int:id>/',views.delete_student),
    path('student_update/<int:id>/',views.student_update),




    
]


