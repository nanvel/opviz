from enum import Enum


class ContractType(str, Enum):
    CALL = "CALL"
    PUT = "PUT"


class TransactionType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
