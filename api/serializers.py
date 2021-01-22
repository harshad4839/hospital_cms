from rest_framework import serializers
from .models import Docter1, Dignosis, Patient2

class DocterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docter1
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient2
        fields = '__all__'

class DignosisSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    docter = DocterSerializer()
    class Meta:
        model = Dignosis
        fields = '__all__'
