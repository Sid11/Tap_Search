from django.conf.urls.static import static
from django.urls import path, include

from TapSearch import settings
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add',views.add,name='add'),
    path('search', views.search, name='search'),
    path('image',views.image, name='image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)