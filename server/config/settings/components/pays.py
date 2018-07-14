INSTALLED_APPS += (
    'service.payment',
    'payments', 
)

PAYMENT_HOST = 'localhost:8000'
PAYMENT_USES_SSL = False
PAYMENT_MODEL = 'payment.Payment'
PAYMENT_VARIANTS = {
    'default': ('payments.paypal.PaypalProvider', {}),
    'dummy': ('payments.dummy.DummyProvider', {}),
}
