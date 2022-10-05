from rest_framework import status

# TemplateResponse that takes unrendered content
#  and uses content negotiation 
# to determine the correct content type to return to the client.
from rest_framework.response import Response


#api_view defines which method is allowed i.e is it a GET,PUT,POST,DELETE,PATCH
# and works with function based views
from rest_framework.decorators import api_view

from .serializer import studentsSerializers 
from students.models import students
# Create your views here.


from rest_framework.permissions import IsAuthenticated

#function for getting all students in te database
@api_view(['GET'])
def get_students(request):
    try:
        allstudents = students.objects.all()
        serializedstudents = studentsSerializers(allstudents,many=True)
        return Response(serializedstudents.data)    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
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
def delete_student(request,id):
    studentobject = students.objects.get(pk=id)
    allstudents = students.objects.all()
    serializedstudents = studentsSerializers(allstudents ,many=True)
    studentobject.delete()
    return Response(serializedstudents.data, status=status.HTTP_200_OK)  