from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('',views.home_view,name="home"), 
    path('singup/',views.signup,name="singup"),
    path('fileupload/',views.fileUpload,name="file-upload") 
    ]