from .payment_processor import YiPaymentProcessor

class PaymentFactory:
    @staticmethod
    def get_payment_processor(method_id: int, **kwargs):
        if method_id == 1:  # assuming '1' corresponds to '易支付'
            return YiPaymentProcessor(**kwargs)
        # Add more conditions for other payment methods
        raise ValueError(f"Unsupported payment method ID: {method_id}")
