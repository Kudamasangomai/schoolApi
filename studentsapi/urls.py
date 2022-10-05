from django.urls import path
from  . import views

urlpatterns = [
    path('students/',views.get_students,name="students"),
    path('students/<int:pk>/',views.get_detailed_student,name="student-detail"),
    path('student_create/',views.student_create),
    path('student_delete/<int:id>/',views.delete_student),
    path('student_update/<int:id>/',views.student_update)
]
