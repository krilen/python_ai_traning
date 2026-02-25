def sum_of_three(a: int =0, b: int =0, c: int =0) -> int:
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        return 0

    return a +b +c

print(sum_of_three())
print(sum_of_three(1))
print(sum_of_three(1,2))
print(sum_of_three(1,2, 3))

print(sum_of_three("hello"))
