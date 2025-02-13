from senzing import SzError

from . import sz_product

try:
    result = sz_product.get_license()
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
