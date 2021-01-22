"""docter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from api import views
from cms import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home',),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    path('docter/', views.docter, name='docter'),
    path('patient/', views.patient, name='patient'),
    path('docterdetails/', views.docterdetails, name='docterdetails'),

    path('viewpatients/', views.viewpatients, name='viewpatients'),
    path('patientlist/<int:item_pk>/', views.patientlist, name='patientlist'),
    path('patientdignosis/<int:item_pk>/', views.patientdignosis, name='patientdignosis'),
    path('patientlist/<int:item_pk>/delete/', views.deleteitem, name='deleteitem'),

    path('deleteitem/', views.deleteitem, name='deleteitem'),



    path('api-auth', include('rest_framework.urls')),
    path('api/', include('api.urls')),

    # Todos
    # path('', views.home1, name='home'),

]
