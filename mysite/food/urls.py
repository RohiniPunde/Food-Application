from .import views
from django.urls import path


app_name='food'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name="index"),
    path('item',views.item,name="item"),
    #/food/1
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    #add item
    path('create_item',views.CreateItem.as_view(),name='create_item'),
    #edit item
    path('update/<int:id>/',views.update,name='update_item'),
    #delete item
    path('delete/<int:id>/',views.item_delete,name='item_delete'),

]


