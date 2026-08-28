class Solution:
    def countBits(self, n: int) -> List[int]:
        map = {i: 0 for i in range(n + 1)}
        powers_of_two = set()

        map[0] = 0
        mapper_variable = 1
        while mapper_variable <= n:
            powers_of_two.add(mapper_variable)
            map[mapper_variable] = 1
            mapper_variable <<= 1

        last_seen_power_of_two = 2
        for number in range(3, n + 1):
            if number in powers_of_two:
                last_seen_power_of_two = number
                continue
            else:
                diff = number - last_seen_power_of_two
                map[number] = map[diff] + map[last_seen_power_of_two]

        return list(map.values())

            
    def number_of_bits(self, n: int) -> int:
        number = 0
        while n:
            if n & 1:
                number += 1
            n >>= 1
        return number