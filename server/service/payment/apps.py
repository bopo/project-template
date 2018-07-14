from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'service.payment'
    verbose_name = '支付模块'

    def ready(self):
    	pass
