from rest_framework.serializers import ModelSerializer
from students.models import students



class studentsSerializers(ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'