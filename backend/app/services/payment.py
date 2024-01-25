from .payments.payment_factory import PaymentFactory
from ..models.payment_methods import PaymentMethod

class PaymentService:
    async def process_payment(self, payment_request):
        payment_method = await PaymentMethod.get(payment_request.method_id)
        processor = PaymentFactory.get_payment_processor(payment_method.id, **payment_method.details)
        return await processor.process_payment(payment_request)
