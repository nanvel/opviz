from decimal import Decimal
from typing import List

import matplotlib.pyplot as plt

from opviz.constants import ContractType, TransactionType
from opviz.models import Option


class Plotter:
    def __init__(self, title="Options Risk Graph"):
        self.title = title

    def plot(self, spot_price: Decimal, options: List[Option]):
        plt.figure(figsize=(10, 6))
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16], alpha=0.5)
        plt.axhline(color="k", linestyle="--")
        plt.axvline(x=2, color="r", linestyle="--", label="spot price")
        plt.legend()
        plt.legend(loc="upper right")
        plt.title(self.title)
        # plt.fill_between(
        #     x, y, 0, alpha=0.2, where=y > y0, facecolor="green", interpolate=True
        # )
        # plt.fill_between(
        #     x, y, 0, alpha=0.2, where=y < y0, facecolor="red", interpolate=True
        # )
        plt.tight_layout()
        plt.show()

    def calculate_profit(self, prices: List[Decimal], option: Option):
        result = []
        if option.contract_type == ContractType.CALL:
            for price in prices:
                if price > option.strike:
                    result.append(price - option.strike - option.premium)
                else:
                    result.append(-option.premium)
        elif option.contract_type == ContractType.PUT:
            for price in prices:
                if price < option.strike:
                    result.append(option.strike - price - option.premium)
                else:
                    result.append(-option.premium)
        else:
            raise ValueError(f"Invalid contract type: {option.contract_type}")

        if option.transaction_type == TransactionType.SELL:
            result = [-r for r in result]

        return result * option.quantity
