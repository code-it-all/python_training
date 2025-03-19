# this code will lead to circular dependency

# import module_b
#
# def func_a():
#     return "Function A"
#
# print(module_b.func_b())

# solution code we will use lazy import i.e. import when you need.
def func_a():
    return "Function A"

def use_func_b():
    import module_b  # Import inside the function which delays the import
    return module_b.func_b()

if __name__ == "__main__":
    print(use_func_b())