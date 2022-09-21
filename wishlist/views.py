import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from wishlist.models import BarangWishlist
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register_wishlist(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user_wishlist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # Melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) # Membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # Membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user_wishlist(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Danendra Herdiansyah',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "wishlist.html", context)

# Mengembalikan data berbentuk XML
def show_wishlist_xml(request):
    data_barang = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("xml", data_barang), content_type="application/xml")

# Mengembalikan data berbentuk JSON
def show_wishlist_json(request):
    data_barang = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("json", data_barang), content_type="application/json")

# Mengembalikan data berdasarkan ID terhadap XML/JSON
def show_wishlist_xml_by_id(request, id):
    data_barang = BarangWishlist.objects.filter(pk=id)
    
    return HttpResponse(serializers.serialize("xml", data_barang), content_type="application/xml")

def show_wishlist_json_by_id(request, id):
    data_barang = BarangWishlist.objects.filter(pk=id)
    
    return HttpResponse(serializers.serialize("json", data_barang), content_type="application/json")