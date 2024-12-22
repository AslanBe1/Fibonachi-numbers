class Fibonacci:
    def __init__(self,limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        else:
            result=self.a
            temp  = self.b + self.a
            self.a = self.b
            self.b = temp
            return result

fibo = Fibonacci(10)
for i in fibo:
    print(i)