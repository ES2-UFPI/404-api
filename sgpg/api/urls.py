from django.urls import path
from . import views


urlpatterns = [
    path('portais/', views.PortalList.as_view(), name='Portal-list'),
    path('portal/<int:pk>', views.PortalDetail.as_view(), name='portal-detail'),
]