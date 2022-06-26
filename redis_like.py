class Redis:
    def __init__(self):
        self.storage = {}
        self.rollback_actions = []
        self.in_transaction = False

    def get(self, key):
        # Big O = constant
        return self.storage[key] if key in self.storage else "NULL"
    
    def set(self, key, value):
        # Big O = constant
        if self.in_transaction:
            if key in self.storage:
                value = self.storage[key]
                self.rollback_actions.append((
                    self.set,
                    (
                        key,
                        value
                    )
                ))
            else:
                self.rollback_actions.append((
                    self.unset,
                    (key)
                ))
        self.storage[key] = value
        
    def unset(self, key):
        # Big O = constant
        if self.in_transaction:
            if key in self.storage:
                value = self.storage[key]
                self.rollback_actions.append((
                    self.set,
                    (
                        key,
                        value
                    )
                ))
        self.storage.pop(key, None)
    
    def num_equal_to(self, value):
        # Big O =  N
        # N: values lenght  
        count = 0
        for storage_key, storage_value in self.storage.items():
            if value == storage_value:
                count += 1
        return count

    def beggin(self):
        # Big O = constant
        self.in_transaction = True

    def commit(self):
        # Big O = constant
        self.rollback_actions = []
        self.in_transaction = False

    def rollback(self):
        # Big O = N 
        # N: rollback_actions lenght
        rollback_actions = self.rollback_actions
        self.commit()
        for (function, params) in reversed(rollback_actions):
            if len(params)>1:
                function(params[0], params[1])
            else:
                function(params[0])