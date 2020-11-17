import xmlrpc.client

# class teste:
#     def add(self, a, b):
#         return a + b

s = xmlrpc.client.ServerProxy('http://localhost:8000')

# s = teste()

print(s.pow(2,3))  # Returns 2**3 = 8
print(s.add(2,3))  # Returns 5
print(s.mul(5,2))  # Returns 5*2 = 10

# Print list of available methods
print(s.system.listMethods())


