# TODO Найдите количество книг, которое можно разместить на дискете
v_d=1.44
count_list=100
count_str=50
count_char=25
v_char=4
all_char=count_char*count_str*count_list
v_all_char=all_char*v_char
v_d_b=v_d*1024*1024
count=int(v_d_b//v_all_char)
print("Количество книг, помещающихся на дискету:", count)
