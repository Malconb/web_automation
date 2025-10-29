class SoftAssert:
    def __init__(self):
        self.errors = []

    def verify(self, condition, msg):
        try:
            assert condition, msg
        except AssertionError as e:
            self.errors.append(str(e))

    def assert_all(self):
        if self.errors:
            raise AssertionError("Soft asserts fallaron:\n" + "\n".join(self.errors))
