from decimal import Decimal

from opviz.plotter import Plotter
from opviz.constants import ContractType, TransactionType
from opviz.models import Option


def main():
    option = Option(
        contract_type=ContractType.CALL,
        transaction_type=TransactionType.BUY,
        strike=Decimal(102),
        premium=Decimal(2),
    )

    options = [
        Option(
            contract_type=ContractType.CALL,
            transaction_type=TransactionType.SELL,
            strike=Decimal(215),
            premium=Decimal("7.63"),
        ),
        Option(
            contract_type=ContractType.CALL,
            transaction_type=TransactionType.BUY,
            strike=Decimal(220),
            premium=Decimal("5.35"),
        ),
        Option(
            contract_type=ContractType.PUT,
            transaction_type=TransactionType.SELL,
            strike=Decimal(210),
            premium=Decimal("7.2"),
        ),
        Option(
            contract_type=ContractType.PUT,
            transaction_type=TransactionType.BUY,
            strike=Decimal(205),
            premium=Decimal("5.52"),
        ),
    ]

    plotter = Plotter()
    plotter(spot_price=Decimal("212.26"), options=options)


if __name__ == "__main__":
    main()
