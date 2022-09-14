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

def show_wishlist_xml(request):
    data_barang = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("xml", data_barang), content_type="application/xml")

def show_wishlist_json(request, id):
    data_barang = BarangWishlist.objects.filter(pk=id)
    
    return HttpResponse(serializers.serialize("json", data_barang), content_type="application/json")