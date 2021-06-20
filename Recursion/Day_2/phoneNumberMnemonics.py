res = []
Map= { 
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv", 
    "9": "wxyz"
    }

def Mnenomics(digits, index, currentStr):
    if len(digits) == len(currentStr):
        res.append(currentStr)
        return
    for c in Map[digits[index]]:
        Mnenomics(digits, index + 1, currentStr + c)

Mnenomics(input("Enter Digits: ") , 0, "")
print(res)