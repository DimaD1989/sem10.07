# # 📌Создайте класс-функцию, который считает факториал числа при вызове экземпляра. 📌Экземпляр должен запоминать последние k значений. 📌Параметр k передаётся при создании экземпляра. 📌Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
# import json
# from collections import defaultdict
#
#
# class Factorial:
#
#     def __init__(self):
#         self.results = defaultdict(list)
#         self.termkresults = []
#         self.kresults = []
#
#     def __call__(self, number):
#         result = 1
#         for i in range(1, number + 1):
#             result *= i
#         self.results[number].append(result)
#         self.termkresults.append(result)
#         if number < len(self.termkresults):
#             for i in range(len(self.termkresults) - number, len(self.termkresults)):
#                 self.kresults.append(self.termkresults[i])
#         else:
#             for i in range(0, len(self.termkresults)):
#                 self.kresults.append(self.termkresults[i])
#
#     def __str__(self):
#         txt = '\n'.join((f'{k}: {v}' for k, v in self.results.items())) + "\n" + '\n'.join(
#             (f' {v}' for v in self.kresults))
#         return txt
#
#         def __enter__(self):
#
#             return self
#
#         def __exit__(self, exc_type, exc_val, exc_tb):
#             new_file = open("manager_file.json", "w", encoding="utf-8")
#             json.dump(self.results, new_file, indent=4, ensure_ascii=False)
#             new_file.close()
#
# factor = Factorial()
#
# factor(1)
# factor(10)
# factor(3)
# factor(2)
#
# print(factor)
# with factor as new_file:
#     new_file(10)
#
#
# # 📌Доработаем задачу 1. 📌Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
#
# 📌Создайте класс-генератор. 📌Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step. 📌Если переданы два параметра, считаем step=1. 📌Если передан один параметр, также считаем start=1.

# 📌Создайте класс-генератор. 📌Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step. 📌Если переданы два параметра, считаем step=1. 📌Если передан один параметр, также считаем start=1.


# class MyGenarator:
#
#
#     def __init__(self, *args):
#         start, stop, step, result = 1, 1, 1, 1
#         if len(args) == 1:
#             stop = args[0]
#         elif len(args) == 2:
#             start = args[0]
#             stop = args[1]
#         elif len(args) == 3:
#             start = args[0]
#             stop = args[1]
#             step = args[2]
#         else:
#             raise AttributeError
#
#         if start < stop:
#             self.start = start
#             self.stop = stop
#             self.step = step
#             self.result = result
#             self.iter_step = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.result *= (self.start + self.step * self.iter_step)
#
#         if self.start + self.step * self.iter_step >= self.stop:
#             raise StopIteration
#         self.iter_step += 1
#         return self.result
#
#
# my_gener = MyGenarator(10, 51, 10)
# for i in my_gener:
#     print(i)
#
# 📌Доработайте класс прямоугольник из прошлых семинаров. 📌Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных). 📌Используйте декораторы свойств.

