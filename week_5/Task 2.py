class ParseError(Exception):
    """ Error while parsing file """

    def __init__(self, *args, line_no=None, text=None):
        super().__init__(*args)
        self.line_no = line_no
        self.text = text

    def __str__(self):
        if self.line_no is None and self.text is None:
            return super().__str__()
        if self.line_no is not None and self.text is None:
            return f"cannot parse text on line {self.line_no}"
        if self.line_no is None and self.text is not None:
            return f"cannot parse text: '{self.text}'"
        if self.line_no is not None and self.text is not None:
            return f"cannot parse text on line {self.line_no}: '{self.text}'"


raise ParseError(text='...')