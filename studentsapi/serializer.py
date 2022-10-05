from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from students.models import students
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True



class studentsSerializers(ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'



class Registerserializer(ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','password2']
        extra_kwargs ={
            'password':{'write_only':True}
        }
    

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
    
        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        user.set_password(password)
        user.save()
        return user
  