my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for a, b in enumerate(my_list):
    if b.replace(" + ", " ").replace(" - ", " ").isdigit():
        if b.isdigit():
            my_list[a] = f" '{int(b):02}' "
        else:
            my_list[a] = f" '{b[0]}{int(b[1:]):02}', "
print(my_list)
print(" ".join(my_list))
