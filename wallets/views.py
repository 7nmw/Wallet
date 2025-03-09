from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wallet
from .serializers import WalletSerializer
from django.shortcuts import get_object_or_404

class WalletsPOSTAPIView(APIView):
    '''
    POST запрос с 2 операциями DEPOSIT и WITHDRAW,
    '''
    def post(self, request, wallet_uuid):
        # проверка наличия кошелька
        wallet = get_object_or_404(Wallet, id_uuid=wallet_uuid)
        serializer = WalletSerializer(data=request.data)

        # проверка валидности json
        if not serializer.is_valid():
            return Response(serializer.errors)

        # операции по изменению счета в кошельке
        operation_type = request.data.get('operationType')
        amount = request.data.get('amount')
        if operation_type == 'DEPOSIT':
            wallet.balance += abs(amount)
        elif operation_type == 'WITHDRAW':
            if wallet.balance < amount:
                return Response({'error': 'Недостаточно средств', 'balance': wallet.balance})
            else:
                wallet.balance -= abs(amount)

        wallet.save()

        return Response({'message': 'Операция прошла успешно', 'balance': wallet.balance})


class WalletsGETAPIView(APIView):
    '''
    Get запрос для получения баланса кошелька
    '''
    def get(self, request, wallet_uuid):
        wallet = get_object_or_404(Wallet, id_uuid=wallet_uuid)
        return Response({"balance": wallet.balance})
