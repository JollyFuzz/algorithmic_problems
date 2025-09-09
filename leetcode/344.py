"""
https://leetcode.com/problems/reverse-string/description/
"""
def solution1(s):
    return s[::-1]
    

def solution(s):
    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:
        s[p1], s[p2] = s[p2], s[p1]

        p1 += 1
        p2 -= 1

    return s


if __name__ == "__main__":
    cases = [
        ["h","e","l","l","o"],
        []
    ]

    for c in cases:
        expected_result = c[::-1]

        result = solution(c)

        print(f"{ result == expected_result } - { c } - {result}")