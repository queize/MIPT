from solution import Solution
solution = Solution()

def test1() -> None:
    nums = [
        [1,2,3,4],
        [1,1,1,1,1],
        [3,1,2,10,1]
    ]

    for number in nums:
        test = solution.runningSum(number)
        print(number, ' \t||\t ', test)

def test2() -> None:
    accounts = [
        [[1,2,3],[3,2,1]],
        [[1,5],[7,3],[3,5]],
        [[2,8,7],[7,1,3],[1,9,5]]
    ]

    for acc in accounts:
        print(solution.maximumWealth(acc))


def test3() -> None:
    N = range(16)

    for n in N:
        print(solution.fizzBuzz(n), f'\tn = {n}')

def test4() -> None:
    N = [
        14, 8, 123
    ]

    for n in N:
        print(solution.numberOfSteps(n), f'|| n = {n}')

def test5() -> None:
    ransomNote = "aa"
    magazine = "aba"
    print(solution.canConstruct(ransomNote=ransomNote, magazine=magazine))


if __name__ == '__main__':
    test5()
