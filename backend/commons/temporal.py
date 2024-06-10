class TemporalEntity:
    def __init__(self):
        self.event = ""
        self.year = ""
        self.date = ""
        self.context_before = ""
        self.context_after = ""

    def __str__(self):
        return self.date + " | " + self.year + " :: " + self.event