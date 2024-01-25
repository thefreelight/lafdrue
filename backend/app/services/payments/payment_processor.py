from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    async def process_payment(self, payment_request):
        pass

class YiPaymentProcessor(PaymentProcessor):
    # initialize with credentials and other necessary details
    def __init__(self, merchant_id, secret_key, payment_gateway):
        self.merchant_id = merchant_id
        self.secret_key = secret_key
        self.payment_gateway = payment_gateway

    async def process_payment(self, payment_request):
        # Implement the payment processing logic here
        pass
