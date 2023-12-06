"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path
from store.views import index,get_blog_articles,offers,get_offers_data   
from accounts.views import signup, logout_user,login_user
from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('get_blog_articles/',get_blog_articles,name='get_blog_articles'),
    path('offers/',offers,name='offers'),
    path('get_offers_data/',get_offers_data,name='get_offers_data'),
    path('signup/',signup,name='signup'),
    path('logout/',logout_user,name='logout'),
    path('login/',login_user,name='login'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
