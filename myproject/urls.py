"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from tech1.views import *
from tech4.views import *
from tech3.views import *
from tech2  import urls as csv_app_urls
from tech5.views import *
from django.conf import settings
from django.conf.urls.static import static
from tech7.views import *
from tech8 import views
from jewellery.views import *
from kaggle.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/',fn1,name="fn1"),
    path('myprofile/',fn2,name="fn2"),
    path('m/',fn6,name="fn6"),
    path('sjson/',jsondata,name="jsondata"),
    path('csv/', include(csv_app_urls)),
    path('upload/',upload,name='upload'),
    path('read/',detail,name='detail'),
    path('admin/', admin.site.urls),
    path("", include("tech8.urls")),
    path('gold/',material,name="matrial"),
    path('salary/',salarydata,name="salarydata"),

   
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

