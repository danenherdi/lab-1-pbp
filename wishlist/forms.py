from django.forms import ModelForm
from wishlist.models import BarangWishlist

class AddWishlistForm(ModelForm):
    class Meta:
        model = BarangWishlist
        fields = ['nama_barang', 'harga_barang', 'deskripsi']