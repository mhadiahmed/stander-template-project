from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class FileUplad(models.Model):
    user = models.ForeignKey(User,related_name="user_uploads",on_delete=models.CASCADE)
    fiels_uploads = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
