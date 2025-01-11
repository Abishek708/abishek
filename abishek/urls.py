from django.urls import path
from . import views

app_name = 'abishek'

urlpatterns = {
    path("", views.about, name='about'),
    path("resume.html",views.resume,name='resume'),
    path("project.html", views.project, name='project'),
    path("experience.html", views.experience, name='exp')
}