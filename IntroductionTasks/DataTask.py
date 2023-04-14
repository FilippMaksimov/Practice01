string1 = "This is a string"
string2 = "This is another string"
string3 = "hello"
string4 = "This is a string with used spacing in the end            "
string5 = "        Text"
string6 = "     Text2       "
print(string1 + ". " + string2)
# len() - длина строки
print(len(string1))
# title() - преобразует первый символ каждого слова в строке к верхнему регистру
print(string3.title())
# lower() - символы строки преобразуются к нижнему регистру
# upper() - символы строки преобразуются к верхнему регистру
print(string3.upper() + " " + string1.lower())
# rstrip() - удаляются пробелы в конце строки
print(string4.rstrip() + " " + string3)
# lstrip() - удаляются пробелы в начале строки
print(string5.lstrip())
# strip() - удаляются пробелы с обоих концов
print(string6.strip())
# strip('0') - удаляются с обоих концов указанные символы в параметре функции
print(string3.strip('h'))

d = "qwerty"
# Извлекается символ ‘e’
ch = d[2]
print(ch)

chm = d[1:3]
print(chm)
chm = d[1:]
print(chm)
chm = d[:3]
print(chm)
chm = d[:]
print(chm)
# Вывести каждые 2 на отрезке от индекса 1 (включительно) до 5 (не включительно)
chm = d[1:5:2]
print(chm)

a = 5
b = 10
res_dev = b / a
res_remainder = b % a
res_power = a ** 3
print(res_dev, res_remainder, res_power)

param = "string" + str(15)
print(param)
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " =", "{:3.2f}".format(n3))

a = 1/3
print("{:7.3f}".format(a))
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print(dir(list1))
help(list1.insert)
help(list1.append)
help(list1.sort)
help(list1.remove)
help(list1.reverse)
list1[0] = 72
print(list1)
list1.append(13)
print(list1)
list1.insert(1, 73)
print(list1)
list1.__delitem__(len(list1) - 1)
list1.__delitem__(1)
print(list1)

list1.sort(reverse=True)
print(list1)
list2 = [3, 5, 6, 2, 33, 6, 11]
lis = sorted(list2)
print(list2, lis)

print(dir(tuple))
help(tuple.index)
help(tuple.count)
seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
# Количество элементов в кортеже со значением 8
print(seq.count(8))
# Номер индекса элемента со значением 44
print(seq.index(44))
listseq = list(seq)
print(type(listseq))

# Dictionaries
D = {"food": "Apple", "quantity": 4, "color": "Red"}
D["quantity"] += 10
print(D["food"], D["quantity"])
dp = {}
dp.__setitem__("Name", input("Enter the Name: "))
dp.__setitem__("Age", input("Enter the Age: "))
print(dp)

rec = {"name": {"firstname": "Bob", "lastname": "Smith"},
       "job": ["dev", "mgr"],
       "age": 25}
rec["job"].append("janitor")
print(rec["name"], "\n", "firstname: ", rec["name"].__getitem__("firstname"),
      "\n", rec["job"])





