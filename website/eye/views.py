from django.http import HttpResponse
from .models import Picture
from django.template import loader
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def index(request):
	return render(request, 'eye/index.html', {})

def result(request):
    if request.method == 'POST' and request.FILES['eyeimage']:
        
        import os
        PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
        CAPTHA_ROOT = os.path.join(PROJECT_PATH,'test_images','uploaded','uploaded.jpg')
        os.remove(CAPTHA_ROOT)
        
        myfile = request.FILES['eyeimage']
        fs = FileSystemStorage()
        filename = fs.save('uploaded.jpg', myfile)
        uploaded_file_url = fs.url(filename)
        
        uploaded_file_url = os.path.join(PROJECT_PATH,'test_images', 'uploaded', 'uploaded.jpg')
        
        from .classifier import prediction
        tested, percent = prediction()
        
        return render(request, 'eye/results.html', {
            'tested': tested, 'percent' : percent, 'uploaded_file_url' : uploaded_file_url
        })
    
    
    return render(request, 'eye/results.html')