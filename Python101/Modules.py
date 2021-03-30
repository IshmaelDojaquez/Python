# Modules is separating code into multiple files

import Converters  # Do not need to add the extensions... aka .py int necessary
from Converters import kg_to_lbs  # you can import specific functions


print(Converters.kg_to_lbs(70))
kg_to_lbs(100)

