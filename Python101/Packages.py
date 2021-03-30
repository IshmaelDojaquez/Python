# A way to organize code. Container for multiple modules

import ecommerce.shipping  # importing the whole directory
from ecommerce.shipping import calc_shipping  # importing the exact function
from ecommerce import shipping  # importing the whole module

ecommerce.shipping.calc_shipping()
calc_shipping()
calc_shipping()
calc_shipping()
shipping.calc_shipping()