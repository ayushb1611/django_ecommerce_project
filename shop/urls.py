from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('log_out',views.log_out,name='log_out'),
    path('index/',views.index,name='index'),
    path('change_password/',views.change_password,name='change_password'),
    path('register',views.register,name='register'),
    path('forget_pass',views.forget_pass,name='forget_pass'),
    path('terms',views.terms,name='terms'),
    path('about',views.about,name='about'),
    path('ownerlogin',views.ownerlogin,name='ownerlogin'),
    path('log__out',views.log__out,name='lolog__outg_out'),
    path('ownerindex',views.ownerindex,name='ownerindex'),
    path('add_products',views.add_products,name='add_products'),
    path('product_list',views.product_list,name='product_list'),
    path('update_product/<int:id>',views.update_product,name='update_product'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('cart/<int:id>',views.cart,name='cart'),
    path('showcart',views.showcart,name='showcart'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('usercartlist',views.usercartlist,name='usercartlist'),
    path('customer_data',views.customer_data,name='customer_data'),
    path('profile',views.profile,name='profile'),
    
    
    
    
    # path('reset_password',auth_views.PasswordResetView.as_view(),name="reset_password"),
    # path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(),name="reset_password_done"),
    # path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="reset_password_confirm"),
    # path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name="reset_password_complete"),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

