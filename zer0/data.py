# Link - 0
# Account - 1
# Flag	 - 2
# Date	- 3
# Payee	- 4
# Category Group: Category - 5
# Category Group - 6
# Category	- 7
# Memo	- 8
# Outflow	- 9
# Inflow	- 10
# Cleared - 11


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
