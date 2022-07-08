class Solution:
    def fib(self, n: int) -> int:
        five = sqrt(5)
        fi = (1 + five)/2 
        alph = (1-five)/2

        return int(( fi**n -  alph**n )/  five)