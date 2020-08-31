from django.shortcuts import render,redirect
from django.http import HttpResponse
from cv.models import ContactDetails


# Create your views here.
def cv_page(request):
    if request.method == 'POST':
        ContactDetails.objects.create(text=request.POST['contact_detail'])
        return redirect('/cv')

    contacts = ContactDetails.objects.all()
    return render( request, 'cv.html', {
                'contacts': contacts,
                })
