#
#
# REMEMBER TO CHANGE VERSION NUMBER IN "setup.py" WHEN MODIFYING CODE


def validate_nzbn(nzbn):
    if len(nzbn) == 13:
        return True
    else:
        return False
