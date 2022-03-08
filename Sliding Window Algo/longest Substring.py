"""
Data created : 03-02-2022
@Abhisek
"""

"""
Problem : Find the longest substring of a string containing k distinct characters
"""


class subString:
    def __init__(self):
        pass

    def simpleApproach(self, s, k):
        n = len(s)
        maxString = ''
        for i in range(n):
            for j in range(i, n):
                t = s[i:j+1]
                if len(set(t)) == k and len(t) > len(maxString):
                    maxString = max(t, maxString)
        return maxString


if __name__ == '__main__':
    st = ['abcdbdbdbddc','abcbdbdbbdcdabd']
    s = subString()
    t = 1
    for each in st:
        print(f"******************TEST CASE {t}*********************")
        print(f"Output of running all the algos on the string {each} are:")
        print("Simple Approach:", s.simpleApproach(each, 3))
        # print("Dynamic Approach:", sol.dynamicProgram(a))
        # print("Kadane's Solution", sol.kadaneSolution(a))
        t += 1
