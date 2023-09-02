from django.urls import path
from . import views

urlpatterns = [
    # path('',views.product_alt_view),
    # path('',views.product_alt_view),
    path('',views.SearchListView.as_view(),name='search'),
    
    
    
]
