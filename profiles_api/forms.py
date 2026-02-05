from django import forms
from profiles_api import models

class UserRegisterForm(forms.ModelForm):
    # Şifre alanına yazılanlar görünmesin (*** olsun) diye widget ekledim
    password = forms.CharField(widget=forms.PasswordInput, label="Şifre")

    class Meta:
        model = models.UserProfile
        fields = ['name', 'email', 'password'] # Formda görünecek alanlar

    def save(self, commit=True):
        # Form kaydedilirken araya giriyorum.
        # Amacım: Şifreyi veritabanına düz metin olarak değil, şifreli (hash) kaydetmek.
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user
