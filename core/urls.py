from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path('', views.index, name="homepage"),
   
    path('product/<slug>/', views.ItemDetailView.as_view(), name="product"),
    
]
