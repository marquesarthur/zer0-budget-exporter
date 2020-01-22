from zer0.adapter.ca.cibc import CibcAdapter
from zer0.adapter.ca.tangerine import TangerineAdapter


class BankCsvReader(object):
    def __init__(self, reader):
        self.reader = reader

    def to_zer0(self, data):
        return self.reader.to_zer0(data)

    @staticmethod
    def get_reader(bank):
        valid_banks = {
            "cibc": BankCsvReader(CibcAdapter()),
            "tangerine": BankCsvReader(TangerineAdapter()),
        }
        return valid_banks[bank]
