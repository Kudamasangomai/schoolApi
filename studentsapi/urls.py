from unicodedata import name
from django.urls import path
from  . import views
from .views import(

  get_students_view
    

)

from rest_framework.authtoken.views  import obtain_auth_token
urlpatterns = [

    #creating its own app is better
    path('register_user/',views.register_user),


    #login user
    path('login/',obtain_auth_token,name="login"),

    path('',views.routes,name="routes"),  
    path('api/students/',views.get_students,name="students"),
    path('api/student/<int:pk>/',views.get_detailed_student,name="student-detail"),
    path('api/student_create/',views.student_create),
    path('api/student_delete/<int:id>/',views.delete_student),
    path('api/student_update/<int:id>/',views.student_update),
    path('api/student_search/<studinfo>/',views.search_student),


    path('api/students_view/',get_students_view.as_view(),name="students_view"),




    
]


