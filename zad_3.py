def if_even(n) -> bool:
    return n % 2 == 0


flag = if_even(5)

print("Liczba parzysta") if flag else print("Liczba nieparzysta")
