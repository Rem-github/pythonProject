
# Эта программа выводит типы данных записанных в списке

dif_type = [8,2.5,'simple string',[1,2],(2,3),{3,4},None]
print(dif_type)
for i in range(len(dif_type)):
    print(f'{dif_type[i]} это {type(dif_type[i])}')
