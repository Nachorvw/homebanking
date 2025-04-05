from django.shortcuts import render

def wallets_view(request):
    return render(request, 'coins/my_wallets.html')

def coin_details_view(request):
    return render(request, 'coins/coin_details.html')

def portfolio_view(request):
    return render(request, 'coins/portfolio.html')
