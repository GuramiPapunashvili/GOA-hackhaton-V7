def swap_luwi_kenti(lst):
    for i in range(0, len(lst), 2):

        lst[i], lst[i + 1] = lst[i + 1], lst[i]

print(swap_luwi_kenti([4, 6, 3, 8, 7, 4, 6, 9]))