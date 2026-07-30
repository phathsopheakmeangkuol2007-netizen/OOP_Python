class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def check_password(self, input_password):
        return self.password == input_password
u1 = User("alice", "secure123")
print(u1.check_password("secure123"))
print(u1.check_password("helloworld"))