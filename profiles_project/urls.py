from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views # Django'nun hazır giriş/çıkış sistemini kullandım
from profiles_api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- Döküman İşlemleri ---
    path('', views.index, name='index'), # Ana sayfa
    path('create/', views.document_create, name='document_create'),

    # <int:pk> kısmı önemli: Hangi dökümanı açacağımızı ID numarasından anlıyoruz
    path('document/<int:pk>/', views.document_detail, name='document_detail'),
    path('document/<int:pk>/delete/', views.document_delete, name='document_delete'),

    # --- Üyelik İşlemleri ---
    path('register/', views.register, name='register'),

    # Login ve Logout için ekstra view yazmaya gerek yok, Django'nun hazır olanları iş görüyor
    path('login/', auth_views.LoginView.as_view(template_name='profiles_api/login.html'), name='login'),

    # Çıkış yapınca direkt login sayfasına yönlendirsin (next_page='login')
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
