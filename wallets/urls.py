from django.urls import path
from .views import WalletsPOSTAPIView, WalletsGETAPIView


urlpatterns = [
    # Эндпоинт для выполнения операций с кошельком
    path('api/v1/wallets/<uuid:wallet_uuid>/operation', WalletsPOSTAPIView.as_view()),
    # Эндпоинт для получения баланса
    path('api/v1/wallets/<uuid:wallet_uuid>', WalletsGETAPIView.as_view()),
]
