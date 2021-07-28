from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from .forms import LoginForm
urlpatterns = [
  
   # path('',views.index,name='shop/index'),
  path('',views.ProductView.as_view(), name=('index')),
  
  # path('home',views.home,name=('index')),
   path('home',views.ProductView.as_view(), name=('index')),
   path('product',views.saveproduct,name='product'),
   path('about',views.ProductView3.as_view(),name=('about')),
   #path('contact',views.contactview,name=('contact')),
   #path('contact',views.contactview.as_view(), name=('contact')),
   path('contact',views.savecontact1,name='contact'),
   #path('mens',views.mens,name=('mens')),
   path('mens',views.ProductView1.as_view(), name=('mens')),
   #path('womens',views.womens,name=('womens')),
   path('login',views.login,name=('login')),
   path('womens',views.ProductView2.as_view(), name=('womens')),
   #path('single',views.single,name=('single')),
   path('single/<int:pk>',views.productdetailview.as_view(), name='single'),
   path('index1',views.index1,name=('index1')),
   path('edit/<str:pk>', views.edit_data, name='edit'),
   path('delete/<int:id>', views.del_product, name='delete'),
   path('edit1/<str:pk>', views.edit_contact, name='edit1'),
   path('delete1/<int:id>', views.del_contact, name='delete1'),
   path('checkout',views.checkout,name=('checkout')),
   path('cart/', views.show_cart, name='showcart'),
   path('pluscart/', views.plus_cart),
   path('minuscart/', views.minus_cart),
   path('removecart/', views.remove_cart),
   path('emptycart',views.emptycart,name=('emptycart')),
   path('accounts/login/', auth_views.LoginView.as_view(template_name='shop/login.html', 
   authentication_form=LoginForm), name='login'),
   path('logout/' , auth_views.LogoutView.as_view(next_page='login'),name='logout'),
   path('profile',views.ProfileView.as_view(),name=('profile')),
   path('placeorder',views.placeorder,name=('placeorder')),
   path('paymentdone', views.payment_done, name=('paymentdone')),
   path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
   path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

 ] + static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)