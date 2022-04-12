from django.contrib import admin
from django.urls import path, include
from online.views import index, product_detail, add_to_cart, cart, delete_cart
from bouchbon import settings
from django.conf.urls.static import static
from online.models import Product
from comptes.views import registration, logout_user, login_user


urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),

    path('registration/', registration, name="registration"),
    path('logout/', logout_user, name="logout"),
    path('cart/', cart, name="cart"),
    path('cart/', delete_cart, name="delete_cart"),
    path('connexion/', login_user, name="connexion"),
    path('product/<str:slug>/', product_detail,  name="product"),
    path('product/<str:slug>/add-to-cart', add_to_cart,  name="add-to-cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
