class Redis:
    def __init__(self):
        self.storage = {}
        self.rollback_actions = []
        self.in_transaction = False

    def get(self, key):
        return self.storage[key] if key in self.storage else "NULL"
    
    def set(self, key, value):
        if self.in_transaction:
            self.rollback_actions.append((self.set),key,None)
        self.storage[key] = value
        
    def unset(self, key):
        self.storage.pop(key, None)
    
    def num_equal_to(self, value):
        count = 0
        for storage_key, storage_value in self.storage.items():
            if value == storage_value:
                count += 1
        return count
