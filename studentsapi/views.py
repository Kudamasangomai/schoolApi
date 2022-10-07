from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes

from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.models import Token


from .serializer import studentsSerializers,Registerserializer 
from students.models import students
from django.db.models  import Q


from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination



@api_view(['GET'])
@permission_classes([AllowAny,])
def routes(request):
    api_routes ={

        
	        'Students List Without Pagination':'/api/students/',
            'Students List With pagination':'/api/students_view/',
			'Student detail':'api/student/id/',
			'Student Create':'/api/student_create/',
			'student Update':'/contact_update/id',
			'student Delete':'/api/student_delete/id/',
            'student search': '/api/student_search/<lastname>/',
            

    }
    return Response(api_routes)


@api_view(['POST',])
def register_user(request):
    if request.method == 'POST':
        newsuser = Registerserializer(data=request.data)
        data = {}
        if newsuser.is_valid():
            user_acc = newsuser.save()
            data['reponse'] = "Registration Succesfully  completed"
            data['email'] = user_acc.email
            data['username'] = user_acc.username
            token = Token.objects.get(user=user_acc).key
            data['token'] = token
        else:
            return Response(newsuser.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)


#function for getting all students in the database
@api_view(['GET'])
@permission_classes([AllowAny,])
def get_students(request):
    try:
        allstudents = students.objects.all()
        serializedstudents = studentsSerializers(allstudents,many=True)
        return Response(serializedstudents.data)    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

class get_students_view(ListAPIView):
    queryset = students.objects.all()
    serializer_class = studentsSerializers
    authentican_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)
    pagination_class = PageNumberPagination

@api_view(['GET'])
@permission_classes([AllowAny,])
def get_detailed_student(request,pk):
    try:
        studentobject = students.objects.get(id=pk)
        students_serialized_object = studentsSerializers(studentobject,many=False)
        return Response(students_serialized_object.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def student_create(request):
	newstudentobj = studentsSerializers(data=request.data)
	if newstudentobj.is_valid():
		newstudentobj.save()
		return Response(newstudentobj.data, status=status.HTTP_201_CREATED)
	return Response(newstudentobj.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def student_update(request,id):
		studentobject = students.objects.get(pk=id)
		serializer = studentsSerializers(instance=studentobject, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated,])
def delete_student(request,id):
    studentobject = students.objects.get(pk=id)
    allstudents = students.objects.all()
    serializedstudents = studentsSerializers(allstudents ,many=True)
    studentobject.delete()
    return Response(serializedstudents.data, status=status.HTTP_200_OK)  

@api_view(['GET'])
@permission_classes([AllowAny,])
def search_student(request,studinfo):

    searchedstudent = students.objects.filter(
        Q(lastname__contains = studinfo)|
        Q(firstname__contains = studinfo) 
        )
    students_serialized_object = studentsSerializers(searchedstudent,many=True)
    return Response(students_serialized_object.data)