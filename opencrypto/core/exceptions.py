"""
OpenCrypto — Custom Exception Hierarchy

Framework-specific exceptions for precise error handling.
All exceptions inherit from OpenCryptoError so users can catch
any framework error with a single except clause.
"""


class OpenCryptoError(Exception):
    """Base exception for all OpenCrypto errors."""


class DataFetchError(OpenCryptoError):
    """Raised when market data cannot be retrieved from any endpoint.

    Attributes:
        symbol: The trading pair that failed (if applicable).
        source: Which data source was attempted (e.g. "binance_futures").
    """

    def __init__(self, message: str, *, symbol: str = "", source: str = ""):
        self.symbol = symbol
        self.source = source
        super().__init__(message)


class ManipulationDetectedError(OpenCryptoError):
    """Raised when ShieldGuard blocks a trade due to manipulation risk.

    Attributes:
        risk_score: The computed manipulation risk score (0-100).
        warnings: List of individual check descriptions that triggered.
    """

    def __init__(self, message: str, *, risk_score: int = 0, warnings: list[str] | None = None):
        self.risk_score = risk_score
        self.warnings = warnings or []
        super().__init__(message)


class StrategyImplementationError(OpenCryptoError):
    """Raised when a user-provided strategy fails to meet the BaseStrategy contract.

    Common causes:
    - Missing ``name`` or ``version`` attributes.
    - ``generate_signal()`` returns an invalid type.
    - Signal has logically impossible levels (SL above entry for LONG, etc.).
    """


class BacktestError(OpenCryptoError):
    """Raised for errors during backtest execution (insufficient data, etc.)."""
