#!/usr/bin/python3
"""
    this function determines the winner of a game
    args:
        x - number of rounds
        num - an array of n(any integer)

    Return:
        string: representing the winner
"""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        current_player = "Maria"
        remaining_nums = set(range(2, n + 1))
        while True:
            possible_moves = set()
            for num in remaining_nums:
                if is_prime(num):
                    possible_moves.add(num)
                    for multiple in range(num * 2, n + 1, num):
                        possible_moves.discard(multiple)
            if not possible_moves:
                break
            move = max(possible_moves)
            remaining_nums.difference_update(set(range(move, n + 1, move)))
            if current_player == "Maria":
                current_player = "Ben"
            else:
                current_player = "Maria"
        if current_player == "Maria":
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] == wins["Ben"]:
        return None
    elif wins["Maria"] > wins["Ben"]:
        return "Maria"
    else:
        return "Ben"
