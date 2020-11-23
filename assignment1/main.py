### Assignment 1

# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)
initial_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Initial list: {0}".format(initial_list))

# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
sorted_list = sorted(initial_list)
print("Sorted list: {0}".format(sorted_list))

# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
descending_list = sorted(initial_list, reverse=True)
print("Descending: {0}".format(descending_list))

# afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print("Even: {0}".format(sorted_list[1::2]))

# afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print("Odd: {0}".format(sorted_list[::2]))

# afișarea elementelor multipli ai lui 3.
print("multiples of 3: {0}".format(sorted_list[2::3]))
