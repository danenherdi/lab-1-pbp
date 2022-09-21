from django.urls import path
from wishlist.views import show_wishlist, show_wishlist_xml, show_wishlist_xml_by_id, show_wishlist_json, show_wishlist_json_by_id, register_wishlist, login_user_wishlist, logout_user_wishlist


app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name='show_wishlt_xml'),
    path('json/', show_wishlist_json, name ='show_wishlist_json'),
    path('xml/<int:id>', show_wishlist_xml_by_id, name='show_wishlist_xml_by_id'),
    path('json/<int:id>', show_wishlist_json_by_id, name='show_wishlist_json_by_id'),
    path('register/', register_wishlist, name='register'),
    path('login/', login_user_wishlist, name='login'),
    path('logout/', logout_user_wishlist, name='logout'),
]