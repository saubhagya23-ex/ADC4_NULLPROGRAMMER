from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import House
from django.template import Template, Context


def index(request):
    return render(request, template_name="Home.html",
                  context={"house": House.objects.all})


def register(request):
    form = UserCreationForm()
    return render(request, "register.html",
                  context={'form': form})


def sign_in(request):
    form = UserCreationForm()
    return render(request, "sign_in.html", )


def header(request):
    return render(request, 'header.html', )


def view_Booking_lists(request):
    list_of_Houses = House.objects.all()
    print(list_of_Houses)
    context_variable = {
        'booking': list_of_Houses
    }
    return render(request, 'register.html', context_variable)


def register(request):
    return render(request, 'register.html')


def booking_save(request):
    if request.method == 'POST':
        get_all = request.POST
        get_House_location = request.POST['House Location']
        get_Buyer_name = request.POST['Buyer Name']
        get_Buyer_contact = request.POST['Buyer Contact']
        get_Seller_name = request.POST['Seller Name']
        get_Seller_contact = request.POST['Seller Contact']
        Booking_obj = House(House_location=get_House_location, Buyer_name=get_Buyer_name,
                            Buyer_contact=get_Buyer_contact, Seller_name=get_Seller_name,
                            Seller_contact=get_Seller_contact)
        Booking_obj.save()
        return HttpResponse("Record saved")
    else:
        return HttpResponse("Error record saving")


def booking_update_forms(request, ID):
    print(ID)
    book_obj = House.objects.get(id=ID)
    print(book_obj)
    context_variable = {
        'book': book_obj
    }
    return render(request, 'bookingsupdateform.html', context_variable)


def booking_update_save(request, ID):
    book_obj = House.objects.get(id=ID)
    print(book_obj)
    book_form_data = request.POST
    print(book_form_data)
    book_obj.House_location = request.POST['House Location']
    book_obj.Buyer_name = request.POST['Buyer Name']
    book_obj.Buyer_contact = request.POST['Buyer Contact']
    book_obj.Seller_name = request.POST['Seller Name']
    book_obj.Seller_contact = request.POST['Seller Contact']
    book_obj.save()

    return HttpResponse("Record Updated!!")


def delete_book(request, ID):
    book_obj = House.objects.get(id=ID)
    House.objects.filter(id=ID).delete()

    return HttpResponse("Deleted SUccessfully!!")
