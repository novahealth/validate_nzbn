def validate_nzbn(nzbn):
    if len(nzbn) == 13 and nzbn[0] == 9:
        return True
    if nzbn is None:
        return None
    else:
        return False
