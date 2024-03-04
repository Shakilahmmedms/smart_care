from rest_framework import serializers
from .models import Doctor,Specialization,Designation,AvailbeTime,Review

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    specialization = serializers.StringRelatedField(many = True)
    designation = serializers.StringRelatedField(many = True)
    availbe_time = serializers.StringRelatedField(many = True)
    class Meta:
        model = Doctor
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class AvailbeTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailbeTime
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'