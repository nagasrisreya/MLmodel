
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path('',include('basic.urls')),
    path('',include('irisApp.url')),
    path('admin/', admin.site.urls),

]
