from utils import Utils

def testFunction(actual, expected):
    if(actual == expected):
        print("Pass")
        return 1
    else:
        print(f"Fail. Actual {actual}, Expected {expected}")
        return 0

tester = Utils()

print("######### Reversed Tests #########")
reversedScore = 0
reversedScore += testFunction(tester.reversed(10327), 72301)
reversedScore += testFunction(tester.reversed("String test"), -1)
reversedScore += testFunction(tester.reversed(23.35654), -1)
reversedScore += testFunction(tester.reversed("QWERTY"), -1)
reversedScore += testFunction(tester.reversed(-0.23894), -1)
reversedScore += testFunction(tester.reversed(0), 0)
reversedScore += testFunction(tester.reversed(9823), 3289)
reversedScore += testFunction(tester.reversed(-100), -1)

print(f"Final Score = {reversedScore}/8")

print("######### Formatter Tests #########")
formatterScore = 0
formatterScore += testFunction(tester.formatter(8), ('0b1000', '0o10'))
formatterScore += testFunction(tester.formatter(1823), ('0b11100011111', '0o3437'))
formatterScore += testFunction(tester.formatter("String test"), -1)
formatterScore += testFunction(tester.formatter(23.35654), -1)
formatterScore += testFunction(tester.formatter("QWERTY"), -1)
formatterScore += testFunction(tester.formatter(-0.23894), -1)
formatterScore += testFunction(tester.formatter(0), ('0b0', '0o0'))
formatterScore += testFunction(tester.reversed(-100), -1)

print(f"Final Score = {formatterScore}/8")