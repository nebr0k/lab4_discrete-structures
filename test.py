import unittest
from itertools import permutations, combinations


class Test(unittest.TestCase):

    def test_permutations(self):
        for n in range(1, 5):
            expected_result = set("".join(str(x) for x in perm) for perm in permutations(range(1, n + 1)))
            result = set()
            for perm in permutations(range(1, n + 1)):
                result.add("".join(str(x) for x in perm))
            self.assertEqual(result, expected_result)

    def test_combinations(self):
        for n in range(1, 5):
            for r in range(1, n + 1):
                expected_result = set(combi for combi in combinations(range(1, n + 1), r))
                result = set()
                for combi in combinations(range(1, n + 1), r):
                    result.add(tuple(combi))
                self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

