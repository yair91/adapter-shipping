from shipping_adapter.checkout import Checkout
from shipping_adapter.legacy_carrier import LegacyCarrier
from shipping_adapter.legacy_carrier_adapter import LegacyCarrierAdapter


def test_checkout_quotes_through_legacy_carrier_adapter():
    checkout = Checkout(LegacyCarrierAdapter(LegacyCarrier()))

    price = checkout.shipping_quote("45000", 10.0)

    assert price == LegacyCarrier().get_price("45000", 22.0462)
    assert price == 33.56
