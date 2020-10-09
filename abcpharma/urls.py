from django.urls import path
from . import views

#path arranged alphabetically by name
app_name= 'abcpharma'
urlpatterns=[
    #path('api/data', views.get_data, name='api-data'),

    #TEST URL
    path('index', views.CustomerIndexView.as_view(), name="index_view"),
    path('dashboard', views.DashboardIndexView.as_view(), name="dashboard_view"),
    path('customer-registration', views.CustomerRegistrationView.as_view(), name="customer_registration_view"),
    path('medicine-registration', views.MedicineRegistrationView.as_view(), name="medicine_registration_view"),
    path('order',views.CustomerOrderView.as_view(), name="order_view"), 
]