
from django.urls import path, include
from api import views

urlpatterns = [
    path('docter/', views.Docter.as_view(), name="docter_api"),
    path('patient/', views.Patient.as_view(), name="Patient"),
    path('dignosis/', views.Dignosis.as_view(), name="Dignosis"),

    ]