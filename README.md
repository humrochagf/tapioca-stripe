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

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
- Explore this package using iPython
- Have fun!
