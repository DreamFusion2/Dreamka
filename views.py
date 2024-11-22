from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def page(request):
    return render(request, "main/page.html")

def page2(request):
    return render(request, "main/page2.html")   #визуализация сна

def page3(request):
    return render(request, "main/page3.html")   #страница загрузки

def page4(request):
    return render(request, "main/page4.html")   #зарегесирируйтесь

def page5(request):
    return render(request, "main/page5.html")   #войдите

def page6(request):
    return render(request, "main/page6.html")   #присоединитесь к нам
