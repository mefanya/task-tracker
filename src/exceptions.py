class ZeroRunTimeTask(Exception):
    def __init__(self, massage=None):
        super().__init__(massage)
