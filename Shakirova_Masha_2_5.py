my_list = [57.8, 46.51, 97, 45.54, 65, 123.25, 26.3, 534.58, 23.50, 153, 14.2, 26.84, 26.45, 278.45, 453.43, 45.34,
           123.45, 4.4, 43, 51.68, 13.5, 15.51, 54.68, 78.64, 14.68, 78.6, 4.1, 658.4, 68.46, 85.4, 16.84, 68.4, 1.53]
for a in my_list:
    r, c = str(f"{a:.2f}").split(".")
    print(f"{r} рублей {int(c):02d} копеек;")
