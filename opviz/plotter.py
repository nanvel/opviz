from decimal import Decimal
from typing import List

import matplotlib.pyplot as plt

from opviz.models import Option


class Plotter:
    def __init__(self, title="Options Risk Profile"):
        self.title = title

    def __call__(
        self, spot_price: Decimal, options: List[Option], padding=Decimal("0.1")
    ):
        prices = [spot_price]
        [prices.append(option.strike) for option in options]
        if padding:
            prices.append(max(prices) * (1 + padding))
            prices.append(min(prices) * (1 - padding))
        prices.sort()

        plt.figure(figsize=(10, 6))
        plt.title(self.title)
        plt.tight_layout()
        plt.axhline(color="k", linestyle="--")
        plt.axvline(x=spot_price, color="r", linestyle="--", label="Spot price")

        values_sum = []
        for option in options:
            values = []
            for price in prices:
                pnl = option.get_pnl(price)
                values.append(pnl)
            plt.plot(prices, values, alpha=0.5, label=str(option))
            if not values_sum:
                values_sum = values
            else:
                values_sum = [v1 + v2 for v1, v2 in zip(values_sum, values)]

        plt.plot(prices, values_sum, alpha=1, label="Combined")

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

        plt.legend(loc="upper right")

        plt.show()
