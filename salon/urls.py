from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Клиенты
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),
    
    # Мастера
    path('masters/', views.MasterListView.as_view(), name='master_list'),
    path('masters/<int:pk>/', views.MasterDetailView.as_view(), name='master_detail'),
    path('masters/create/', views.MasterCreateView.as_view(), name='master_create'),
    path('masters/<int:pk>/update/', views.MasterUpdateView.as_view(), name='master_update'),
    path('masters/<int:pk>/delete/', views.MasterDeleteView.as_view(), name='master_delete'),
    
    # Услуги (Price)
    path('prices/', views.PriceListView.as_view(), name='price_list'),
    path('prices/<int:pk>/', views.PriceDetailView.as_view(), name='price_detail'),
    path('prices/create/', views.PriceCreateView.as_view(), name='price_create'),
    path('prices/<int:pk>/update/', views.PriceUpdateView.as_view(), name='price_update'),
    path('prices/<int:pk>/delete/', views.PriceDeleteView.as_view(), name='price_delete'),
    
    # Записи
    path('appointments/', views.AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/create/', views.AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/<int:pk>/update/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name='appointment_delete'),
    
    # Услуги (Service)
    path('services/', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    
    # Отзывы
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/add/', views.add_review, name='add_review'),
]