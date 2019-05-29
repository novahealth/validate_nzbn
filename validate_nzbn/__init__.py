#
#
# REMEMBER TO CHANGE VERSION NUMBER WHEN MODIFYING CODE


def validate_nzbn(nzbn):
    if len(nzbn) == 13 and nzbn[:1] == 9:
        return True
    if nzbn is None:
        return "empty"
    else:
        return False
