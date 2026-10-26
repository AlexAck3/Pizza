number_of_pies = int(input("enter the number of pies:"))
size_of_pies = int(input("enter the size: 12, 14, 16:" ))

total_flour_ratio = 1
flour_percent = .57
f_0102_ratio = .7
f_bread_ratio = .2
f_semoline_ratio = 0.05
f_wholeweat_ratio = 0.05
water_ratio = 0.69
idy_ratio = 0.004
sugar_ratio = 0.01
salt_ratio = 0.02
evoo_ratio = 0.03
poolish_flour_ratio = .3 # 30% of total flour, equal parts water
dought_weight = 0

if size_of_pies == 14:
    dough_weight = 300
elif size_of_pies == 12:
    dough_weight = 200
elif size_of_pies ==16:
    dough_weight = 400
else:
    print("please enter a dough weight in the listed sizes")
    size_of_pies = int(input("enter the size: 12, 14, 16:" ))

total_flour = dough_weight * flour_percent
f_0102 = total_flour * f_0102_ratio
f_bread = total_flour * f_bread_ratio
f_semolina = total_flour * f_semoline_ratio
f_wholeweat = total_flour * f_wholeweat_ratio
water = total_flour * water_ratio
idy = total_flour * idy_ratio
sugar = total_flour * sugar_ratio
salt = total_flour * salt_ratio
evoo = total_flour * evoo_ratio

f_poolish = poolish_flour_ratio * total_flour
water_poolish = f_poolish
idy_poolish = .25 * idy

f_0102_pizza = f_0102 - f_poolish
water_pizza = water - water_poolish
idy_pizza = idy - idy_poolish


print(round(total_flour), round(f_0102), round(f_bread), round(f_semolina), round(f_wholeweat), round(water), round(idy,1), round(sugar), round(salt), round(evoo))

