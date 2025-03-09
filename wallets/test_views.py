import unittest
from rest_framework.test import APITestCase
from rest_framework import status
from wallets.models import Wallet


class WalletTests(APITestCase):

    # Создаем тестовый кошелек
    def setUp(self):
        self.wallet = Wallet.objects.create(id_uuid='123e4567-e89b-12d3-a456-426614174000', balance=1000)

    # Тест get запроса
    def test_get_wallet_balance(self):
        url = "https:///api/v1/wallets/123e4567-e89b-12d3-a456-426614174000"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"balance": 1000 })


    # Тест пополнения кошелька
    def test_post_deposit(self):
        payload = {
            "operationType": "DEPOSIT",
            "amount": 21
        }
        url = "https:///api/v1/wallets/123e4567-e89b-12d3-a456-426614174000/operation"
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Операция прошла успешно", "balance": 1021})

    # Тест снятия кошелька
    def test_post_withdraw(self):
        payload = {
            "operationType": "WITHDRAW",
            "amount": 46
        }
        url = "https:///api/v1/wallets/123e4567-e89b-12d3-a456-426614174000/operation"
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Операция прошла успешно", "balance": 954})



if __name__ == '__main__':
    unittest.main()