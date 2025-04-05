from django.urls import path
from coins.views import wallets_view, coin_details_view, portfolio_view
urlpatterns = [
    path('wallets/', wallets_view, name='wallets'),
    path('details/', coin_details_view, name='details'),
    path('portfolio/', portfolio_view, name='portfolio'),
    
]