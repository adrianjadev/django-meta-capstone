from django.urls import path, include
from .views import homeView, MenuItemViewSet, BookingViewSet

from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'menu', MenuItemViewSet),
router.register(r'booking', BookingViewSet),

urlpatterns = [
    path('', homeView, name="home-view"),
    path('restaurant/', include(router.urls)),
]