def is_prime(func):
    def wrapper(*args):
        result_sum = func(*args)
        if result_sum <= 1:
            print('Сложное')
            return result_sum

        for a in range(2, int(result_sum ** 0.5) + 1):
            if result_sum % a == 0:
                print('Сложное')
                return result_sum

        print('Простое')
        return result_sum
    return wrapper


@is_prime
def sum_three(*args):
    result_sum = sum(args)
    return result_sum


result = sum_three(2, 3, 6)
print(result)
