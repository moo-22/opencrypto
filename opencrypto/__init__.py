"""
OpenCrypto — Modular Algorithmic Trading Framework

An open-source framework for building crypto trading strategies.
Provides market data, risk management, position tracking, backtesting,
and technical analysis tools. Bring your own strategy.
"""

__version__ = "1.0.0"

from opencrypto.core.base_strategy import BaseStrategy, StrategySignal
from opencrypto.core.shield_guard import ShieldGuard
from opencrypto.core.position_manager import PositionManager
from opencrypto.core.data_bridge import DataBridge
from opencrypto.core.exceptions import (
    OpenCryptoError,
    DataFetchError,
    ManipulationDetectedError,
    StrategyImplementationError,
    BacktestError,
)

__all__ = [
    "BaseStrategy",
    "StrategySignal",
    "ShieldGuard",
    "PositionManager",
    "DataBridge",
    "OpenCryptoError",
    "DataFetchError",
    "ManipulationDetectedError",
    "StrategyImplementationError",
    "BacktestError",
]
