__EMPTY_CELL = ""


def next_available_row(wks):
    account_col = wks.get_col(2)
    next_row = sum([1 for c in account_col if c != __EMPTY_CELL])

    return next_row
