class Utils:
    def reversed(self, num):
        if not isinstance(num, int):
            print("Argument is not int")
            return -1
        
        elif num < 0:
            print("Number is negative")
            return -1

        ans = 0
        while(num>0):
            rem = num%10
            ans = ans*10 + rem
            num = num//10

        return ans


    def formatter(self, num):
        if not isinstance(num, int):
            print("Argument is not int")
            return -1
        
        elif num < 0:
            print("Number is negative")
            return -1
        
        return bin(num), oct(num)
