class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digitsToChars = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        result = []

        def backtrack(i, substring):
            if i == len(digits):
                result.append(substring)
                return

            for c in digitsToChars[digits[i]]:
                backtrack(i+1, substring+c)

        backtrack(0, "")
        return result

