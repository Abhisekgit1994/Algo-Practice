"""
Data created : 03-02-2022
@Abhisek
"""

"""
Problem : Find the longest substring of a string containing k distinct characters
"""


class Substring:
    def __init__(self):
        pass

    def simpleApproach(self, s, k):  # Time complexity O(n^2)
        n = len(s)
        maxString = ''
        for i in range(n):
            for j in range(i, n):
                t = s[i:j + 1]
                if len(set(t)) == k and len(t) > len(maxString):
                    maxString = max(t, maxString)
        return maxString

    def slidingWindow(self, s, k):  # Time complexity O(n), Space Complexity O(1)
        pass


if __name__ == '__main__':
    st = ['abcdbdbdbddc', 'abcbdbdbbdcdabdd']
    s = Substring()
    t = 1
    for each in st:
        print(f"******************TEST CASE {t}*********************")
        print(f"Output of running all the algos on the string {each} are:")
        print("Simple Approach:", s.simpleApproach(each, 2))
        # print("Sliding window Solution", s.slidingWindow(each, 2))
        t += 1
