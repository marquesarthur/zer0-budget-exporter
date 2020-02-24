ZER0_COLUMNS = [
    "Link", "Account", "Flag", "Date",
    "Payee", "Category Group: Category",
    "Category Group", "Category",
    "Memo", "Outflow", "Inflow", "Cleared"
]


class Zer0Data(object):

    def __init__(self):
        self.Link = None
        self.Account = None
        self.Flag = None
        self.Date = None
        self.Payee = None
        self.Category_Group_Category = None
        self.Category_Group = None
        self.Category = None
        self.Memo = None
        self.Outflow = None
        self.Inflow = None
        self.Cleared = None

    def to_zer0(self):
        return [
            self.Link if self.Link else "",
            self.Account if self.Account else "",
            self.Flag if self.Flag else "",
            self.Date.strftime('%m/%d/%Y') if self.Date else "",
            self.Payee if self.Payee else "",
            self.Category_Group_Category if self.Category_Group_Category else "",
            self.Category_Group if self.Category_Group else "",
            self.Category if self.Category else "",
            self.Memo if self.Memo else "",
            self.Outflow if self.Outflow else "",
            self.Inflow if self.Inflow else "",
            self.Cleared if self.Cleared else ""
        ]
