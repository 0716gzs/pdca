from typing import Dict


class Receiver(object):

    def __init__(self, account: str, amount: int, type: str = "MERCHANT_ID", description: str = "分账", user_type: str = None):
        self.account = account
        self.amount = amount
        self.type = type
        self.user_type = user_type
        self.description = description

    def to_dict(self) -> Dict:
        data = {}
        if self.account is not None:
            data['account'] = self.account

        if self.amount is not None:
            data['amount'] = self.amount

        if self.type is not None:
            if self.user_type:
                data['type'] = self.user_type
            else:
                data['type'] = self.type

        if self.description is not None:
            data['description'] = self.description

        return data
