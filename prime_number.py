def is_prime(num: int) -> bool:
    if len([i for i in range(1, num + 1) if num % i == 0]) == 2:
        return True
    return False
