"""
Django settings for profiles_project project.
"""

import os

# Proje ana klasör yolu
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Geliştirme aşamasında olduğumuz için güvenlik anahtarı burada durabilir
SECRET_KEY = '3ksd&xhee=o4jtht0x37s27k800ik3vj4#k!bl1c_m!k5((r75'

# Hata ayıklama modu açık (Canlıya alırken False yapılmalı)
DEBUG = True

# Vagrant veya localhosttan erişim sorunu olmasın diye hepsine izin verdim
ALLOWED_HOSTS = ['*']


# Uygulama Tanımları

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # İleride API lazım olursa diye ekli kalsın
    'profiles_api',   # Kendi oluşturduğum uygulama burada
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'profiles_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'profiles_project.wsgi.application'


# Database
# Proje küçük olduğu için şimdilik SQLite kullanıyorum
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Şifre Doğrulama Kuralları (Çok basit şifreleri engeller)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Dil ve Saat Ayarları

LANGUAGE_CODE = 'tr' # Hata mesajları Türkçe olsun

TIME_ZONE = 'Europe/Istanbul' # Türkiye saati

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Statik dosyalar (CSS, JS, Resimler)
STATIC_URL = '/static/'

# --- ÖZEL AYARLAR ---

# Django'nun default user modeli yerine kendi yazdığım modeli kullan
AUTH_USER_MODEL = 'profiles_api.UserProfile'

# Giriş yapınca direkt ana sayfaya (index) yönlendir
LOGIN_REDIRECT_URL = 'index'

# Çıkış yapınca tekrar giriş ekranına (login) dön
LOGOUT_REDIRECT_URL = 'login'
