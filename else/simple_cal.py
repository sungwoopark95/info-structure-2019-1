a = 4.14216281895504
num_a = 1646

b = 4.27227722772277
num_b = 606

c = 4.08361774744027
num_c = 586

d = 4.07971014492754
num_d = 552

data_num = num_a + num_b + num_c + num_d
wavg = (a * (num_a / data_num)) + (b * (num_b / data_num)) + (c * (num_c / data_num)) + (d * (num_d / data_num))
print(wavg)