import pandas as pd
data=pd.read_excel(io='lab_pi_101.xlsx', engine='openpyxl')
ocenka=len(data)-1
k=0
a=set()
b=set()
c=set()
for i in range(ocenka+1):
    if data['Группа'].values[i]=='ПИ101':
        k+=1
        a.add(data['Личный номер студента'].values[i])
        b.add(data['Уровень контроля'].values[i])
        c.add(data['Год'].values[i])
        
        
print('Исходном датасете содеражалось ',ocenka,' оценок, из них' ,k,' относиться к группе ПИ101')
print('Исходном датасете находится ',len(a),' судентасо слудующими личными номерами: ',end="")
for x in a:  
    print(x,', ' ,end="" )
print()
print('Используемый формы контроля: ',end="")
for x in b:  
    print(x,', ', end="")
print()
print('Данные пресдставлены за по следующим учебным годам: ',end="")
for x in c:  
    print(x,', ', end="")