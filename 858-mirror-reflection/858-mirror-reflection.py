class Solution:
    def gcd(self,a,b):
            if a == 0:
                return b
            return self.gcd(b % a, a)
    def lcm(self,a,b):
        return (a / self.gcd(a,b))* b
    def mirrorReflection(self, p,q):
        
        lcm=self.lcm(p,q)
        m=lcm//p
        n=lcm//q
        if n%2==0:
            return 2
        if m%2==0:
            return 0
        return 1
    