from django.shortcuts import render

# Create your views here.



def about(request):
     return render(request, 'index.html')

def project(request):
     return render(request, 'project.html')

def experience(request):
     return render(request, 'experience.html')

def resume(request):
     return render(request, 'resume.html')
