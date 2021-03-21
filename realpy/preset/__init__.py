""" Global Game Settings
    ---
    ```
    from realpy import RsPreset
    ```
"""
from .header import *
from . import header as RsPreset


# TODO: #22 Make a test from preset.
def test():
    print("***** Test → Realpy Settings *****")

    try:
        print(">>> Module of setting: ", RsPreset)
    except Exception as e:
        print("Error: ", e)
        return False
    return True
