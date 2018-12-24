from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.ComputerListView.as_view(), name='computer_list'),
    path('<int:id>/<slug:slug>/', views.ComputerDetailView.as_view(), name='computer_detail'),

    path('addtocard/<int:product_id>/', views.CartView.as_view(), name='addtocard'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('deletecart/', views.delete_cart, name='deletecart'),

    path('computer/create/', views.CreateComputer.as_view(), name='create'),
    path('computer/<int:pk>/edit/', views.EditComputer.as_view(), name='edit'),
    path('computer/<int:pk>/delete/', views.DeleteComputer.as_view(), name='delete'),
]
