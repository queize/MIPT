class Lucas:
    def __init__(self, u0, u1, p, q, n) -> None:
        self.u0 = u0
        self.u1 = u1
        self.p = p
        self.q = q
        self.n = n
        self.u2 = self.p*self.u1 - self.q*self.u0
    
    def __iter__(self) -> None:
        if self.n < 0:
            return None
        yield self.u0
        if self.n == 1:
            return None
        elif self.n == 2:
            yield self.u1
            return None
        
        for _ in range(2, self.n + 1):
            yield self.u2
            self.u2 = self.p*self.u1 - self.q*self.u0
            self.u0 = self.u1
            self.u1 = self.u2


print(list(Lucas(0, 1, 1, -1, 10)))
