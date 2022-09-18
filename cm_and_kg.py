mass_k = 30.6
height_c = 2.6
print(f"The heigh in cm is {height_c} and in metres is {str(height_c/100.0)}.")# при пересечениии порога значения в половину дробной части начинается вычесление с какой-то странной точностью и правильно ли???
#для 30.5 и 2.5 все работает корректно.
print(f"The mass in kg is {mass_k} and in tons is {(mass_k/1000.0)}")
print(mass_k/1000.0)