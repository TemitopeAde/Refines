from django.contrib import admin
from django.urls import path
from source.views import index, index2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('page2/', index2, name="index2")
]
