from .import views

from django.urls import path
app_name='CartApp'
urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name="product_by_cat"),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name="product_cat_detail")
]
