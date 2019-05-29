#
#
# REMEMBER TO CHANGE VERSION NUMBER IN "setup.py" WHEN MODIFYING CODE

import re


def clean_nzbn(nzbn):
    nzbn_clean = re.sub("[^0-9]", "", nzbn)
    return nzbn_clean


def validate_nzbn(nzbn):
    nzbn_to_validate = clean_nzbn(nzbn)

    if len(nzbn_to_validate) == 13:
        if nzbn_to_validate[0] == "9":
            return nzbn_to_validate
    else:
        return nzbn
