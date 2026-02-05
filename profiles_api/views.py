from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Document
from django.contrib.auth import login
from profiles_api.forms import UserRegisterForm

# Ana Sayfa: Kullanıcının kendi dökümanlarını listeler
def index(request):
    # Eğer kullanıcı giriş yaptıysa veritabanından sadece ONUN dökümanlarını çekiyoruz
    if request.user.is_authenticated:
        documents = Document.objects.filter(user=request.user)
    else:
        # Giriş yapmadıysa boş liste gönderiyoruz ki hata vermesin
        documents = []

    return render(request, 'profiles_api/index.html', {'documents': documents})

# Yeni Döküman Oluşturma Fonksiyonu
@login_required # Bu sayfaya sadece üye olanlar girebilsin
def document_create(request):
    if request.method == "POST":
        # Formdan gelen başlık ve içerik verisini alıyoruz
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Veritabanına yeni kaydı oluşturuyoruz.
        # 'user=request.user' diyerek dökümanı o anki kullanıcıya bağlıyoruz.
        Document.objects.create(user=request.user, title=title, content=content)

        # İşlem bitince ana sayfaya yönlendir
        return redirect('index')

    return render(request, 'profiles_api/document_form.html')

# Döküman Detay ve Düzenleme Sayfası
@login_required
def document_detail(request, pk):
    # Dökümanı id'sine (pk) göre bul.
    # user=request.user ekledim ki başkası URL'den id değiştirip başkasının dosyasını görmesin.
    document = get_object_or_404(Document, pk=pk, user=request.user)

    # Eğer "Kaydet" butonuna basıldıysa (POST isteği geldiyse)
    if request.method == "POST":
        # print("Debug: Kaydetme işlemi başladı") <-- Test amaçlı
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Dökümanın yeni bilgilerini güncelliyoruz
        document.title = title
        document.content = content
        document.save()

        return redirect('index')

    return render(request, 'profiles_api/document_detail.html', {'document': document})

# Döküman Silme İşlemi
@login_required
def document_delete(request, pk):
    # Yine user kontrolü yapıyoruz, sadece sahibi silebilir
    document = get_object_or_404(Document, pk=pk, user=request.user)
    document.delete()
    return redirect('index')

# Kayıt Olma Fonksiyonu
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Kayıt olduktan sonra tekrar şifre girmesin, direkt giriş yapmış olsun
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(request, 'profiles_api/register.html', {'form': form})
