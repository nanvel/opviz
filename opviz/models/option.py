from dataclasses import dataclass
from decimal import Decimal

from opviz.constants import ContractType, TransactionType


@dataclass
class Option:
    contract_type: ContractType
    transaction_type: TransactionType
    strike: Decimal
    premium: Decimal
    quantity: int = 1

    def __str__(self):
        return (
            f"{self.transaction_type.value} x{self.quantity} "
            f"{self.contract_type.value} ST:{self.strike} @ {self.premium}"
        )
