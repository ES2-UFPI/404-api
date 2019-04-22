from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClienteList.as_view(), name='cliente-list'),
    path('cliente/<int:pk>', views.ClienteDetail.as_view(), name='cliente-detail'),
    
    path('portais/', views.PortalList.as_view(), name='Portal-list'),
    path('portal/<int:pk>', views.PortalDetail.as_view(), name='portal-detail'),

]