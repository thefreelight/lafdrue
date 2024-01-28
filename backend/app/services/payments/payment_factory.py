# services/payments/payment_factory.py
# 导入日志库

from .yipay_processor import YiPayProcessor
from ...dependencies.database import get_db
from ...models.payment_methods import PaymentMethod


class PaymentFactory:
    # 映射支付方式到对应的处理器类
    processors = {
        'yipay': YiPayProcessor,
        # 可以继续添加其他支付方式的处理器
    }

    @classmethod
    def get_processor(cls, payment_method):
        db = next(get_db())
        config = db.query(PaymentMethod).filter_by(payment_method=payment_method).first()
        if not config:
            raise ValueError(f"No payment config found for {payment_method}")

        # 根据支付方式获取处理器类
        processor_class = cls.processors.get(payment_method)
        if not processor_class:
            raise ValueError(f"No payment processor class found for {payment_method}")

        # 创建处理器实例并传递所需参数
        processor = processor_class(config.merchant_id, config.secret_key, config.payment_gateway)
        return processor
