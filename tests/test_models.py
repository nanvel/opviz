from decimal import Decimal

from opviz.constants import ContractType, TransactionType
from opviz.models import Option


def test_option():
    option = Option(
        contract_type=ContractType.CALL,
        transaction_type=TransactionType.BUY,
        strike=Decimal(102),
        premium=Decimal(2),
    )
    assert option.get_pnl(Decimal(100)) == -2
    assert option.get_pnl(Decimal(105)) == 1
    assert str(option) == "BUY x1 CALL ST:102 @ 2"
