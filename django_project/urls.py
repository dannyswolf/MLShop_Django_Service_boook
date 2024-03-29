"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('login.urls')),
    path('Calendar/', include('Calendar.urls')),
    path('customers/', include('customers.urls')),
    path('machines/', include('machines.urls')),
    path('copiers_log/', include('Copiers_Log.urls')),
    path('services/', include('services.urls')),
    path('spareparts/', include('spareparts.urls')),
    path('warehouse/', include('warehouse.urls')),
    path('admin/', admin.site.urls, name="admin"),
    path('__debug__/', include(debug_toolbar.urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

