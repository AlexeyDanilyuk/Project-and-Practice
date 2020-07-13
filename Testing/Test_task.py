# Написать скрипт для сравнения двух списков с указанием что добавилось в список, что ушло, насколько позиций
# произошло смещение элемента в списке. Порядок элементов важен.
# Список 1: A, B, C, D, E, F, G, H, I, J, K, L, M, N
# Список 2: B, C, D, A, F, E, Z, M, N, J, K, L


def delta_str(lst_one, lst_two):
    delta_lst2 = list(set(lst_one) - set(lst_two))
    delta_lst1 = list(set(lst_two) - set(lst_one))
    if len(delta_lst1) == 1:
        in_str = 'добавился символ'
    else:
        in_str = 'добавились символы'
    if len(delta_lst2) == 1:
        out_str = 'ушёл символ'
    else:
        out_str = 'ушли символы'
    print(f'Во втором списке {in_str} {", ".join(delta_lst1)}, {out_str} {", ".join(delta_lst2)}')

    for i in lst_two:
        if i in lst_one:
            delta_pos = lst_two.index(i) - lst_one.index(i)
            if delta_pos == 0:
                dlt_str = f'остался на прежней позиции'
            elif abs(delta_pos) == 1:
                dlt_str = f'сместился на {delta_pos} позицию'
            elif 2 <= abs(delta_pos) <= 4:
                dlt_str = f'сместился на {delta_pos} позиции'
            else:
                dlt_str = f'сместился на {delta_pos} позиций'
            print(f'Символ {i} ' + dlt_str)
        else:
            print(f'В первом списке нет символа {i}')


lst1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
lst2 = ['B', 'C', 'D', 'A', 'F', 'E', 'Z', 'M', 'N', 'J', 'K', 'L']
delta_str(lst1, lst2)
