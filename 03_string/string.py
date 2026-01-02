num_list = "0123456789"

# below we are doing number first to 6'th index show
slice_num = num_list[:7]

# below we are trying to remove first 3 element
slice_num1 = num_list[3:]

# below 3'rd peramiter doing 2 gor por por value show korar jonno.
# mane hocche. jeheteo 2 dewo ase tai 2 gor por por value show korteche

slice_num2 = num_list[0: 9 : 2]

# show first char use [0]
first_char = num_list[0]

name = "Mehedi Hasan Foysal"

age = 24;

address = "My name is {} and age is {}"

# formate doing dynamic value pass main string 
address = address.format(name, age)

print(address)
