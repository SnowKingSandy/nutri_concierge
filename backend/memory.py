class MemoryBank:
    def __init__(self):
        self.store = {}

    def remember(self, user, msg):
        self.store.setdefault(user, []).append(msg)

    def recall(self, user):
        return self.store.get(user, [])
