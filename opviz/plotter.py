from decimal import Decimal
from typing import List

import matplotlib.pyplot as plt

from opviz.constants import ContractType, TransactionType
from opviz.models import Option


class Plotter:
    def __init__(self, title="Options Risk Profile"):
        self.title = title

    def plot(self, spot_price: Decimal, options: List[Option]):
        prices = [spot_price]
        [prices.append(option.strike) for option in options]
        prices.sort()
        prices_range = (prices[-1] + prices[0]) / 2 / 10
        price_step = prices_range * 2 / 20
        for i in range(20):
            price = prices[0] - prices_range / 2 + price_step * i
            if price not in prices:
                prices.append(price)
        prices.sort()

        plt.figure(figsize=(10, 6))

        values_sum = []
        for option in options:
            values = self.calculate_profit(prices=prices, option=option)
            plt.plot(prices, values, alpha=0.5, label=str(option))
            if not values_sum:
                values_sum = values
            else:
                values_sum = [v1 + v2 for v1, v2 in zip(values_sum, values)]

        plt.plot(prices, values_sum, alpha=1, label="Combined")

        plt.axhline(color="k", linestyle="--")
        plt.axvline(x=spot_price, color="r", linestyle="--", label="spot price")
        plt.legend()
        plt.legend(loc="upper right")
        plt.title(self.title)
        plt.fill_between(
            prices,
            values_sum,
            0,
            alpha=0.2,
            where=[i > 0 for i in values_sum],
            facecolor="green",
            interpolate=True,
        )
        plt.fill_between(
            prices,
            values_sum,
            0,
            alpha=0.2,
            where=[i < 0 for i in values_sum],
            facecolor="red",
            interpolate=True,
        )
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

        return [r * option.quantity for r in result]
