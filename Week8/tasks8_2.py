class ParseError(Exception):
    """ Error while parsing file """

    line_no: int
    text: str

    def __init__(self, line_no: int, text: str) -> None:
        self.line_no = line_no
        self.text = text
    def __str__(self) -> str:
        
