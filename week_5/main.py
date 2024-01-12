def double_print(S: str) -> None:
    if (S == ''):
        raise ValueError('empty string is not allowed')
    print(S)
    print(S)
    return None

double_print('')