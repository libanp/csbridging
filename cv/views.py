from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cv_page(request):
    return render( request, 'cv.html', {
                'new_contact_detail': request.POST.get('contact_detail', ''),
                })
