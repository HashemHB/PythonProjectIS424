from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login_view, name='login'),
    path('signup/',views.signup, name='signup'),
    path('items/products',views.products, name='products'),
    path('item/product/add',views.add , name='add'),
    path('item/product/update',views.update , name='update'),
    path('item/product/update/<int:product_id>',views.update , name='updateProduct'),
    path('item/product/<int:product_id>',views.product , name='product'),
    path('logout/', views.userLogout, name='userLogout'),
    path('delete/<int:product_id>/', views.delete, name='delete'),
    path('delete-purchase/<int:purchase_id>/', views.deleteFromHistory, name='delete-purchase'),
    path('purchase/<int:product_id>/<str:status>', views.purchase, name='purchase'),
    path('history', views.history, name='history'),
    path('updated-purchase/<int:purchase_id>', views.updatedPurchase, name='updated-purchase'),

]