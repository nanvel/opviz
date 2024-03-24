from decimal import Decimal

from opviz.plotter import Plotter
from opviz.constants import ContractType, TransactionType
from opviz.models import Option


def main():
    option = Option(
        contract_type=ContractType.CALL,
        transaction_type=TransactionType.BUY,
        strike=Decimal(102),
        premium=Decimal(10),
    )

    plotter = Plotter()
    plotter.plot(spot_price=Decimal(100), options=[option])


if __name__ == "__main__":
    main()
