from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    # Standart kullanıcı oluşturma fonksiyonunu değiştirdim
    # Çünkü kullanıcı adı yerine email ile giriş yapılmasını istiyoruz
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Kullanıcı için E-posta adresi girmek zorunludur')

        # Emaili küçük harfe çevirip standart hale getiriyoruz
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # Şifreyi veritabanına şifreli (hash) kaydediyor
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        # Admin (Superuser) oluştururken burası çalışıyor
        user = self.create_user(email, name, password)

        user.is_superuser = True # Bütün yetkileri ver
        user.is_staff = True     # Admin paneline girebilsin
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Django'nun kendi user modelini kullanmak yerine özelleştirdim
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # Admin paneli erişimi için

    objects = UserProfileManager()

    # Giriş yaparken 'username' yerine 'email' kullanılacak
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # Email haricinde ismini de zorunlu istiyoruz

    def __str__(self):
        # Obje yazdırılınca email görünsün
        return self.email

class Document(models.Model):
    # Dökümanlar veritabanında bu tabloda tutulacak
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, # Kullanıcı silinirse dökümanları da silinsin
        related_name='documents'
    )
    title = models.CharField(max_length=255) # Başlık kısmı
    content = models.TextField() # İçerik uzun olabileceği için TextField kullandım
    created_at = models.DateTimeField(auto_now_add=True) # Oluşturulma tarihi otomatik atılır
    updated_at = models.DateTimeField(auto_now=True) # Her düzenlemede tarih güncellenir

    def __str__(self):
        return self.title
