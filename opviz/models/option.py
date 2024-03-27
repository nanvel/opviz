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

    def get_pnl(self, price: Decimal) -> Decimal:
        if self.contract_type == ContractType.CALL:
            if price > self.strike:
                pnl = price - self.strike - self.premium
            else:
                pnl = -self.premium
        elif self.contract_type == ContractType.PUT:
            if price < self.strike:
                pnl = self.strike - price - self.premium
            else:
                pnl = -self.premium
        else:
            raise ValueError(f"Invalid contract type: {self.contract_type}")

        if self.transaction_type == TransactionType.SELL:
            pnl *= -1

        return pnl * self.quantity
