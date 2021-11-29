from django.urls import path
from django.contrib import admin
from addresses import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login),
    path('app_login/', views.app_login),
    path('app_register/', views.app_register),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('img_processing/', views.image_upload_view, name='img_process'),
    path('upload/', views.ImageCreateAPIView.as_view(), name='upload'),
    path('hotel/', views.hotel_recommendation, name='hotel'),
    path('restaurant/', views.restaurant_recommendation, name='restaurant'),
    path('landmark/', views.landmark_information, name='landmark')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
