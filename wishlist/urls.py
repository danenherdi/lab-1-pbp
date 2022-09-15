from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_wishlist_xml
from wishlist.views import show_wishlist_json
from wishlist.views import show_wishlist_xml_by_id
from wishlist.views import show_wishlist_json_by_id


app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name='show_wishlt_xml'),
    path('json/', show_wishlist_json, name ='show_wishlist_json'),
    path('xml/<int:id>', show_wishlist_xml_by_id, name='show_wishlist_xml_by_id'),
    path('json/<int:id>', show_wishlist_json_by_id, name='show_wishlist_json_by_id'),
]