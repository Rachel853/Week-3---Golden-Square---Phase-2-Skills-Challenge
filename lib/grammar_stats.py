class GrammarStats():
    def __init__(self):
        self.pass_count = 0
        self.fail_count = 0

    def check(self, text):
        if ((text[0].isupper())) and (text[-1] in ".?!"):
            self.pass_count += 1
            return True
        else:
            self.fail_count += 1
            return False

    def percentage_good(self):
    # Returns:
    #   int: the percentage of texts checked so far that passed the check
    #        defined in the `check` method. The number 55 represents 55%.
        if (self.pass_count + self.fail_count) == 0:
            return 0
        return round(self.pass_count / (self.pass_count + self.fail_count) * 100)
