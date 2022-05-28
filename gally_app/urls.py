from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "gally_app"
urlpatterns = [
    path("",views.index,name="home"),
    path("place/<place>",views.location, name="locate"),
    path("category",views.category, name="categorySearch")
]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)