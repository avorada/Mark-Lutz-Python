type_of_people = 10
x = f"exist {type_of_people} types of people."

bin="Python"
do_not='not'
y = f"Such, who understand {bin}, and such, who {do_not}."# типичная f-строка

print(x)
print(y)

print(f"I say {x}")
print(f"Also i said '{y}'")#

hilarious = False
joke_evalution = "Isn't this funny?! {}"# мы создали "шаблон", чтоб в дальнейшем, если потребуется(например в цикле) в него можно было что-нибудь вставить, с помощью format

print(joke_evalution.format(hilarious))# c помощью методы format вставили  переменную hilarious .

w = " This is left part of str.."
e = "and this is right part of str."

print(w + e)# строки можно складывать, от расположения переменной в выражении зависит результат сложения. 
print(e + w)