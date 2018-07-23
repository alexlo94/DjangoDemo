from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^(?!.)', include('employees.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^employees/', include('employees.urls')),

]
