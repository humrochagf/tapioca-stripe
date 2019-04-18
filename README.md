# Tapioca Stripe

## Installation

```
pip install tapioca-stripe
```

## Documentation

``` python
from tapioca_stripe import Stripe

client = Stripe(
    api_key='sk_test_4eC39HqLyjWDarjtT1zdp7dc',
)

client.charges_list().get()
```

### Stripe file creation endpoint

This endpoint has a special base `api_root`.

If you want to use this endpoint make sure your **tapioca-wrapper** version
is higher than **1.5.1** that has support to [resource aware get_api_root](https://github.com/vintasoftware/tapioca-wrapper/issues/156).

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
- Explore this package using iPython
- Have fun!
