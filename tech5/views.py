from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def upload(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        print(upload_file.name)
        print(upload_file.size)
        fs = FileSystemStorage()
        name = fs.save(upload_file.name,upload_file)
        url = fs.url(name)
        context['url'] = url
        
    return render(request,"upload.html",context)
   
        