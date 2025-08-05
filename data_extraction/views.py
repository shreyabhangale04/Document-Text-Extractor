from django.shortcuts import render
from data_extraction.forms import FileUploadForm
from data_extraction import dataextractor


def homepage(request):
    result = "failed"
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            input_file = request.FILES['input_file']
            result = dataextractor.execute("Invoice", input_file)
            print("Results : Successful")

        context = {
        'form': form, 
        'result': result
        }
    else:
        form = FileUploadForm()

        context = {
        'form': form
        }
    
    return render(request, 'index.html', context)

from django.http import FileResponse

def download_csv(request):
    file_path = "output.csv"
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='output.csv')
