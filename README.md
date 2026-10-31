# Legacy Shipping Quote Adapter — Starter

Small class activity for the **Adapter** pattern.

`Checkout` expects a `ShippingQuoteProvider` with:

```text
quote(destination, weight_kg)
```

A useful legacy dependency already exists, but exposes:

```text
get_price(postal_code, weight_lb)
```

## Your task

1. Implement `LegacyCarrierAdapter`.
2. Do **not** modify `Checkout`, `ShippingQuoteProvider`, or `LegacyCarrier`.
3. Convert kilograms to pounds inside the Adapter (`1 kg = 2.20462 lb`).
4. Add one focused test proving Checkout can use the legacy carrier through the Target contract.
5. Be ready to name one complexity cost introduced by the Adapter.

Use explicit OO design and keep one main class per source file.

## Team workflow

Only one teammate creates the repository from this template. The team repository must be **public** and everyone works in that same repository.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Design notes

| Role | Class |
| --- | --- |
| Target | `ShippingQuoteProvider` |
| Adapter | `LegacyCarrierAdapter` |
| Adaptee | `LegacyCarrier` |
| Client | `Checkout` |

`LegacyCarrierAdapter` implements `quote(destination, weight_kg)` by passing `destination` as the postal code and converting `weight_kg` to pounds (`1 kg = 2.20462 lb`) before calling `get_price`. `Checkout` and `LegacyCarrier` stay untouched.

### Complexity cost

The Adapter adds one more class and one more indirection between `Checkout` and the carrier. The unit conversion now lives in a place `Checkout` cannot see, so a wrong factor or rounding difference (kg vs lb) is easy to miss when reading the call site, and debugging a bad quote means tracing through the Adapter to the legacy API. Every new legacy carrier with a different interface would also need its own Adapter to maintain.
