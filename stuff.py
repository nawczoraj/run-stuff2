# /// script
# dependencies = [
#     "typeshed_client>=2.8.2",
# ]
# ///

import pprint
import sys

import typeshed_client

stdlib_modules = set(sys.stdlib_module_names)

for full_name, path in typeshed_client.get_all_stub_files():
    name, nested, rest = full_name.partition(".")
    if nested:
        continue
    stdlib_modules.discard(name)

pprint.pprint(stdlib_modules)
