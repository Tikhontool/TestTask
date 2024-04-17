from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main),
    re_path(r'^getPicture/$', views.test_api),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# http://localhost:8000/getPicture/?category[]=auto&category[]=trains
