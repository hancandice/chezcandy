from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path('', views.index, name="homepage"),
   
    path('product/<slug:slug>/', views.ItemDetailView.as_view(), name="product"),
    path("item/create/", views.ItemCreate, name="item_create"),
    path("item/modify/<slug:slug>/",
         views.ItemModify, name="item_modify"),
    path('item/delete/<slug:slug>/',
         views.ItemDelete, name="item_delete")   
]
