from django.shortcuts import render

def Main_Page(request):
    return render(request, 'Main_Page.html')
