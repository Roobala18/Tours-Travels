from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # home page route
    path('all-cars/', views.all_cars, name='all_cars'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'), 
    path('domestic/', views.domestic, name='domestic'),
    path('destinations/', views.all_destinations, name='all_destinations'),
    path('destination/<slug:destination_slug>/', views.destination_detail, name='destination_detail'),
    path('generate-pdf/', views.generate_package_pdf, name='generate_package_pdf'),
    path('generate-pdf/<int:package_id>/', views.generate_package_pdf, name='generate_package_pdf'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-package/', views.add_package, name='add_package'),

    path('international', views.home, name='international'),
    path('interdestinations/', views.all_international, name='all_international'),
    path('interdestination/<slug:destination_slug>/', views.destination_detail_inter, name='destination_detail_inter'),

    path('kerala/', views.kerala_view, name='kerala'),
    path('keraladestinations/', views.all_kerala, name='all_kerala'),
    path('kerdestination/<slug:destination_slug>/', views.destination_kerala, name='destination_kerala'),

     
]
