"""
URL configuration for project14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Basic_Form/',Basic_Form,name='Basic_Form'),
    path('Customer_form/',Customer_form,name='Customer_form'),
    path('Product_Form/',Product_Form,name='Product_Form'),
    path('Display_Customer_Details/',Display_Customer_Details,name='Display_Customer_Details'),
    path('Display_Product_Deatils/',Display_Product_Deatils,name='Display_Product_Deatils'),
]
