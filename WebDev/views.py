from django.shortcuts import redirect,render

def BASE(request):
    return render(request, 'base.html')

def HOME(request):
    return render(request, 'Main/home.html')

def COURSE(request):
    return render(request, 'Main/course.html')

def HTML(request):
    return render(request, 'Main/course_html.html')