class Solution(object):
    # @return an integer
    def reverse(self, x):
        xs=str(x)
        xlen=len(xs)
        newx=''
        if xs[0]=='-':
            newx='-'
            for i in range(xlen-1, 0, -1):
                newx+=xs[i]
        else:
            for i in range(xlen-1, -1, -1):
                newx+=xs[i]
        return int(newx) if int(newx) >= -2**31 and int(newx) <= 2**31-1 else 0
