
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'hyundai_app', views.predictionView)
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('forms/', views.cxcontact, name='cxform'),
]