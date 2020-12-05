class BoardingPass:
    def __init__(self, boarding_pass: str):
        self.row_data: str = boarding_pass[:7]
        self.column_data: str = boarding_pass[7:]

    @property
    def row(self) -> int:
        return self._do_binary_operation(one="B", zero="F")

    @property
    def column(self) -> int:
        return self._do_binary_operation(
            one="R", zero="L", row=False
        )

    def _do_binary_operation(
        self, one: str, zero: str, row: bool = True
    ) -> int:
        data = getattr(self, "row_data" if row else "column_data")
        binary_string = data.replace(one, "1").replace(zero, "0")
        return int(binary_string, 2)

    @property
    def seat_id(self):
        return self.row * 8 + self.column
