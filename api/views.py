from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import DocterSerializer, DignosisSerializer, PatientSerializer
from .models import Docter1, Dignosis, Patient2

class Docter(ListCreateAPIView):
    serializer_class = DocterSerializer
    queryset = Docter1.objects.all()

class Patient(ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient2.objects.all()

class Dignosis(ListCreateAPIView):
    serializer_class = DignosisSerializer
    queryset = Dignosis.objects.all()
