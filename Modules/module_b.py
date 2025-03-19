# this code will lead to circular imports

# import module_a
#
# def func_b():
#     print("Function B")

# possible solution code:
def func_b():
    print("Function B")
    return
if __name__ == "__main__":
    import module_a # to prevent a circular import when running module b directly.
    print(module_a.func_a())