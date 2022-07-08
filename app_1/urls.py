
from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home_function),
    path('about',views.about),
    path('quiz',views.quiz),
    path('contact',views.contact),
    path('services',views.services),
    path('register',views.register),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
