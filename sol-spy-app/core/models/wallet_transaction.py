from sqlalchemy import Column, Integer, String, TIMESTAMP, Numeric, ForeignKey, Float,Enum
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from core.models.base import Base
from sqlalchemy.sql import func
from typing import TYPE_CHECKING
from enum import Enum as PyEnum


if TYPE_CHECKING:
    from core.models.tracked_wallet import TrackedWallet

class TransactionStatus(PyEnum):
    PENDING = 'pending'
    SUCCESS = 'success'
    FAILED = 'failed'

class TransactionAction(PyEnum):
    BUY = 'buy'
    SELL = 'sell'
    TRANSFER = 'transfer'

class WalletTransaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    wallet_id: Mapped[int] = mapped_column(ForeignKey("tracked_wallets.id", ondelete='CASCADE'), nullable=False)
    transaction_hash: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    transaction_action: Mapped[TransactionAction] = mapped_column(Enum(TransactionAction),
                                                                  nullable=False)  # "buy" или "sell"
    status: Mapped[TransactionStatus] = mapped_column(Enum(TransactionStatus), nullable=False)
    token_address: Mapped[str] = mapped_column(String, nullable=False)
    token_symbol: Mapped[str] = mapped_column(String)
    buy_amount: Mapped[float] = mapped_column(Float)
    sell_amount: Mapped[float] = mapped_column(Float)
    transfer_amount: Mapped[float] = mapped_column(Float)
    dex_name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Numeric(15,8), nullable=True)
    timestamp: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())

    tracked_wallet: Mapped["TrackedWallet"] = relationship("TrackedWallet", back_populates="transactions")


