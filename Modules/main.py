#1.
#import module_a

#module_a.func_a()
#module_a.use_func_b()

# 2 Dynamic import
# import importlib
#
# def load_and_run(module_name, function_name, *args):
#
#     try:
#         module = importlib.import_module(module_name)
#         func = getattr(module, function_name)
#         result = func(*args)
#         return result
#     except (ImportError, AttributeError) as e:
#         return f"Error: {e}"
#
#
# result_val = load_and_run("my_utils", "multiply", 5, 6)
# print(result_val)  # Output: 30
#
# result_error = load_and_run("nonexistent_module", "some_function")
# print(result_error) # Output: Error: No module named 'nonexistent_module'
#
#
# # 3.
# import calculator
# print(calculator.addition(10, 20))
# print(calculator.subtract(456, 70))
# print(calculator.multipy(568, 7))
# print(calculator.divide(10, 0))
#
#
# # 4
# def module_functions(module, function, *args, **kwargs):
#     try:
#         func = getattr(module, function)
#         return func(*args, **kwargs)
#     except AttributeError:
#         return f"Error: {function} is not defined in {module.__name__}"
#
# print(module_functions(calculator, "addition", 78, 24))

# 5 measuring the import time of a module

import time
start_time = time.time()
from random import randint
end = time.time()
print(f"single module import time: {end - start_time} seconds")

start_time = time.time()
import random
end = time.time()
print(f"package import time: {end - start_time} seconds")

import test

