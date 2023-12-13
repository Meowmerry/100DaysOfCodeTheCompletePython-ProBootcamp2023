# https://peps.python.org/pep-0008/
long_function_name = 0
var_one = 0
var_two = 0
var_three = 0
var_four = 0
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.


def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)


# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Further indentation required as indentation is not distinguishable.


def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
