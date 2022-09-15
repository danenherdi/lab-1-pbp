from multiprocessing import context
from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Danendra Herdiansyah'
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