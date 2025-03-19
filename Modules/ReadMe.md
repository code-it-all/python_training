# Modules and Packages

**1. Investigate Circular Import**:

_What is circular imports?_
- In programming, particularly in Python, a circular import (also known as a circular dependency) occurs when two or more modules depend on each other, creating a loop in their import statements.

Why it's a problem:

- Initialization issues: When Python tries to execute these modules, it can get stuck in a loop, or modules might be only partially initialized, leading to errors.   
- Unpredictable behavior: The order in which modules are loaded becomes critical, and the behavior of your program can become unpredictable.   
- Code complexity: Circular imports make your code harder to understand and maintain.

How to avoid it:

- Refactoring: The best solution is often to refactor your code to eliminate the circular dependency. 
- This might involve: Moving shared code to a separate module.
Reorganizing your code to break the dependency loop.
Rethinking the relationships between your modules.
- Importing within functions: Instead of importing modules at the top of a file, you can sometimes import them inside functions where they are needed. This can delay the import until the module is fully initialized.   
- Using import instead of from ... import: Sometimes using import module_name and then accessing items as module_name.item can help.
- Using importlib: In some complex situations, you can use the importlib module to dynamically import modules at runtime.

Working of Solution:
- When module_a.py is executed, the func_a() definition is processed.
- When use_func_b() is called, module_b.py is imported, and its func_b() is executed.
- Because module_b is only imported when the function is called, the initial circular dependancy is broken.
- When module_b.py is executed, the func_b() definition is processed, and then the if __name__ == "__main__": block is executed. This block then imports module_a, and calls func_a.

**2. Dynamic Module Loading**