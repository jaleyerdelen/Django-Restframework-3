from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
    # related name; user.profile dediğimizde bütün field'lara erişebilmemizi sağlıyor.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile" ) 
    bio = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to="profile_photos/%Y/%m/")

    def __str__(self):
        return self.user.username

    #admin sayfasında başlıklarda ismi profiles olarak geçiyordu profile olarak düzeltmek için;
    class Meta:
        verbose_name_plural = "Profile"

    #user çok yüksek pikselli fotoğraflar yüklememesi için eğer yüklerse 600 piksele düşürüyor
    def save(self, *args, **kwargs):
        #image resize
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.photo.path)


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_message = models.CharField(max_length=240)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Profile Status"

    def __str__(self):
        return str(self.user_profile)
