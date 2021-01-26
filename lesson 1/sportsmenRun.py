
kmFirstDay = int(input("Сколько километров спортсмен пробежал в первый день?: "))
kmTarget = int(input("Для скольки километров делаем расчет?: "))
i = 1
print(f"{i}-й день: {kmFirstDay:.2f} км")
while( kmFirstDay < kmTarget ):
    i +=1
    kmFirstDay = kmFirstDay*1.1
    print(f"{i}-й день: {kmFirstDay:.2f} км")

print(f"Ответ: на {i}-й день спортсмен достиг результата - не менее {kmTarget} км")




