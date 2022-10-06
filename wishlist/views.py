import datetime
import json
from multiprocessing import context
import re
from django import forms
from django.shortcuts import render, redirect
from wishlist.models import BarangWishlist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from wishlist.forms import AddWishlistForm

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


@login_required(login_url='/wishlist/login/')
def show_wishlist_ajax(request):
    if request.method == "POST" :
        new_wishlist = NewWishlist(
            user = request.user,
            nama_barang = form.cleaned_data["nama_barang"],
            harga_barang = form.cleaned_data["harga_barang"],
            deskripsi = form.cleaned_data["deskripsi"]
        )
        new_wishlist.save()
        return redirect("wishlist:show_wishlist_ajax")

    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Danendra Herdiansyah',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "wishlist_ajax.html", context)

@login_required(login_url='/wishlist/login/')
def add_data_ajax(request):
    if request.method == "POST":
        form = AddWishlistForm(request.POST)
        if form.is_valid():
            nama_barang = form.cleaned_data["nama_barang"]
            harga_barang = form.cleaned_data["harga_barang"]
            deskripsi = form.cleaned_data["deskripsi"]

            BarangWishlist.objects.create(nama_barang=nama_barang, harga_barang=harga_barang, deskripsi=deskripsi)

            data_context = {
                "nama_barang": nama_barang,
                "harga_barang": harga_barang,
                "deskripsi": deskripsi
            }

            return JsonResponse(data_context)

# Referensi : https://stackoverflow.com/questions/53594745/what-is-the-use-of-cleaned-data-in-django