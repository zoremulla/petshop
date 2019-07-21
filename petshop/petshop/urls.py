"""petshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Pshopproject import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('Pshopproject/list/',views.pets_list ,name='pets-list'),
    path('Pshopproject/detail/<int:pets_id>/',views.pets_details ,name='pets-details'),
    path('Pshopproject/create/',views.pets_create ,name='pets-create'),
    path('Pshopproject/update/<int:pets_id>/',views.pets_update ,name='pets-update'),
    path('Pshopproject/delete/<int:pets_id>/',views.pets_delete ,name='pets-delete'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)