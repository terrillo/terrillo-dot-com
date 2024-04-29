In Python, a constant is a variable whose value is intended not to change. Constants are typically used to store values that are used frequently in a program, such as mathematical constants or other values that are used throughout the code.

There is no way to directly declare a constant in Python, as the language does not have a keyword or syntax for defining constants. However, there are a few conventions that are often followed to indicate that a variable should be treated as a constant.

One common convention is to use all uppercase letters for the names of constants, with words separated by underscores. For example:



## Using constants in Python

Python constants are often declared and implemented in separate modules/files.

### Using a Module 


**constant.py**

```
PI = 3.14159
```

Using constants


```
import constant

print(constant.PI)
```

```
3.14159
```

## Using Constant module from the python-future

Another convention is to use the constant module from the python-future library, which provides a Constant class that can be used to define constants in a Python program. The Constant class works by raising an exception whenever an attempt is made to change the value of a constant.

```
from constant import Constant

PI = Constant(3.14159)
GRAVITY = Constant(9.8)

PI = 3.14  # Raises a ConstantError exception
```

It's important to note that these conventions are not enforced by the Python interpreter and are only followed as a matter of convention. It's possible to change the value of a constant if you really want to, so it's important to be mindful of this when using constants in your code.