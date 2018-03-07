class DisallowedConnection(Exception):
    # We create a custom exception so that we can get the status code as well.
    # This way, it can be printed when we catch that exception.
    def __init__(self, status):
        self.status = status
