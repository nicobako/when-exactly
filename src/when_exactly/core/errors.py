class InvalidMomentError(RuntimeError):
    """Raised when a moment is invalid."""

    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(f"Invalid Moment: {self.message}")
