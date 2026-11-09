

max_number = max(7, 5, 6, 3, 8, 2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4, 7, 2, 3, 9, 8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

read_letter = input('Enter a letter: ')
print('The entered letter is', read_letter)

string_to_num = int("20303")
print('Number representing the string "20303" is', string_to_num)

binary_str = bin(304)
print('Binary string representing decimal number 304 is', binary_str)

hex_str = hex(304)
print('Hexadecimal string representing decimal number 304 is', hex_str)

euro_unicode = ord('€')
print('Integer representing the Unicode code of the € sign is', euro_unicode)

abs_val = abs(-17)
print('Absolute value of -17 is', abs_val)


# --- 3. Using Modules ---

import math
import random

square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

log_val = math.log(5)
print('Natural logarithm of 5 is', log_val)

sine_val = math.sin(math.radians(90))
print('Sine of 90 degrees is', sine_val)

dice_roll = random.randint(1, 6)
print('Random dice roll:', dice_roll)


# --- 4. Defining a Function ---

# 4.3
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

print('The area of a triangle with sides 3, 4, 5 is', triangle_area(3, 4, 5))
print('The area of a triangle with sides 5, 12, 13 is', triangle_area(5, 12, 13))
print('The area of a triangle with sides 7, 24, 25 is', triangle_area(7, 24, 25))

# 4.4
def sum_digits(number):
    number = abs(number)
    total = 0
    for char in str(number):
        total += int(char)
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')

# 4.5
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade

test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')

# 4.6
def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'
    return result

print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))

# 4.8
def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    elif time_format == '12':
        if hours == 0:
            return f"12:{minutes:02d}am"
        elif hours < 12:
            return f"{hours}:{minutes:02d}am"
        elif hours == 12:
            return f"12:{minutes:02d}pm"
        else:
            return f"{hours - 12}:{minutes:02d}pm"

print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))


# --- 5. Dividing Program Code into Modules (Combined Functions & Tests) ---

# Converters functions
def cm_to_inches(cm):
    return cm / 2.54

def feet_inches_to_cm(feet, inches):
    return (feet * 12 + inches) * 2.54

# Keyboard input functions
def input_string(message):
    val = input(message)
    return val

def input_integer(message):
    val = int(input(message))
    return val

def input_real(message):
    val = float(input(message))
    return val

def input_boolean(message):
    val = input(message)
    return val.lower() == 'y'

# Figures functions
def draw_square(length):
    import turtle
    pen = turtle.Turtle()
    for _ in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length):
    import turtle
    pen = turtle.Turtle()
    for _ in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(length_a, length_b):
    import turtle
    pen = turtle.Turtle()
    for _ in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)


# --- 7. Practice Makes Perfect ---

# 7.3
def month(n):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    if 1 <= n <= 12:
        return months[n - 1]
    return "Invalid month"

print("Enter month number: 9")
print(f"The name of month 9 is {month(9)}")

# 7.4
def count_letter(text, letter):
    return text.count(letter)

sample_text = "You never get a second chance to make a first impression"
print(sample_text)
print(f"The number of letter 'e': {count_letter(sample_text, 'e')}")

# 7.5
def in_range(number, x, y):
    return x <= number <= y

num_test = 7
result_range = in_range(num_test, 2, 15)
print(f"A number: {num_test}")
print(f"Number {num_test} in the range <2,15>: {'yes' if result_range else 'no'}")

# 7.6
def hide(card_number):
    return card_number[:2] + '*' * (len(card_number) - 6) + card_number[-4:]

print(f'f("5290312400019022") returns "{hide("5290312400019022")}"')

# 7.7
def f_binary(binary_number):
    for char in binary_number:
        if char not in '01':
            return False
    return True

print(f'f("101101") returns {f_binary("101101")}')
print(f'f("1311a10100") returns {f_binary("1311a10100")}')

# 7.8
def f_vending(amount_to_pay):
    coins = 0
    coins += amount_to_pay // 5
    amount_to_pay %= 5
    coins += amount_to_pay // 2
    amount_to_pay %= 2
    coins += amount_to_pay
    return coins

print(f'f(23) returns {f_vending(23)}')
print(f'f(8) returns {f_vending(8)}')
print(f'f(2) returns {f_vending(2)}')
print(f'f(0) returns {f_vending(0)}')

# 7.9
def f_sum_digits_even(number, even):
    total = 0
    for char in str(number):
        digit = int(char)
        if even and digit % 2 == 0:
            total += digit
        elif not even and digit % 2 != 0:
            total += digit
    return total

print(f'f(3124,True) returns {f_sum_digits_even(3124, True)}')
print(f'f(3124,False) returns {f_sum_digits_even(3124, False)}')
print(f'f(20576,False) returns {f_sum_digits_even(20576, False)}')
print(f'f(20576,True) returns {f_sum_digits_even(20576, True)}')
print(f'f(13115,True) returns {f_sum_digits_even(13115, True)}')

# 7.10
def f_neg_even(x, y):
    count = 0
    for i in range(x, y + 1):
        if i < 0 and i % 2 == 0:
            count += 1
    return count

print(f'f(-7,8) returns {f_neg_even(-7, 8)}')
print(f'f(-1,11) returns {f_neg_even(-1, 11)}')

# 7.11
def f_any_negative(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0

print(f'f(11,6,-4) returns {f_any_negative(11, 6, -4)}')
print(f'f(5,4,14) returns {f_any_negative(5, 4, 14)}')

# 7.12
def f_asterisks(n):
    return "*/*" * (n - 1) + "*" if n > 0 else ""

print(f'f(4) returns "{f_asterisks(4)}"')
print(f'f(1) returns "{f_asterisks(1)}"')

# 7.13
def f_sequence_str(n):
    res = ""
    for i in range(1, n + 1):
        res += str(i)
    return res

print(f'f(11) returns "{f_sequence_str(11)}"')
print(f'f(4) returns "{f_sequence_str(4)}"')

# 7.14
def f_calc(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2

print(f'f(2,3, "+") returns {f_calc(2, 3, "+")}')
print(f'f(2,3, "%") returns {f_calc(2, 3, "%")}')
print(f'f(2,3, "**") returns {f_calc(2, 3, "**")}')
print(f'f(2,3, "*") returns {f_calc(2, 3, "*")}')
print(f'f(2,3, "-") returns {f_calc(2, 3, "-")}')

# 7.15
def f_detector(detector):
    current = 0
    for char in detector:
        if char == '+':
            current += 1
        elif char == '-':
            current -= 1
        if current >= 3:
            return True
    return False

print(f'f("+-+++-+---") returns {f_detector("+-+++-+---")}')
print(f'f("+-+-+-+-") returns {f_detector("+-+-+-+-")}')
print(f'f("+-++-+--") returns {f_detector("+-++-+--")}')
print(f'f("+-++-++-+---") returns {f_detector("+-++-++-+---")}')

# 7.16
def f_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

print(f'f(5) returns {f_fibonacci(5)}')
print(f'f(9) returns {f_fibonacci(9)}')

# 7.17
def f_palindrome(palindrome):
    return palindrome == palindrome[::-1]

print(f'f("radar") returns {f_palindrome("radar")}')
print(f'f("12-11-21") returns {f_palindrome("12-11-21")}')
print(f'f("book") returns {f_palindrome("book")}')

# 7.18
def f_remove_spaces(sentence):
    return sentence.replace(" ", "")

print(f'f("integrated development environment") returns "{f_remove_spaces("integrated development environment")}"')

# 7.19
def f_sum_repeated(number):
    s = str(number)
    total = 0
    for digit in set(s):
        if s.count(digit) > 1:
            total += int(digit) * s.count(digit)
    return total

print(f'f(1027) returns {f_sum_repeated(1027)}')
print(f'f(230335) returns {f_sum_repeated(230335)}')
print(f'f(513553007) returns {f_sum_repeated(513553007)}')

# 7.20
def f_nth_prime(n):
    count = 0
    current = 1
    while count < n:
        current += 1
        is_p = True
        for i in range(2, int(current**0.5) + 1):
            if current % i == 0:
                is_p = False
                break
        if is_p:
            count += 1
    return current

print(f'f(1) returns {f_nth_prime(1)}')
print(f'f(5) returns {f_nth_prime(5)}')

# 7.21
def f_diff_max_min(n1, n2, n3):
    return max(n1, n2, n3) - min(n1, n2, n3)

print(f'f(7,4,9) returns {f_diff_max_min(7, 4, 9)}')
print(f'f(2,12,8) returns {f_diff_max_min(2, 12, 8)}')

# 7.22
def f_acronym(name):
    words = name.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym

print(f'f("Internet of Things") returns "{f_acronym("Internet of Things")}"')
print(f'f("For Your Information") returns "{f_acronym("For Your Information")}"')
print(f'f("Python") returns "{f_acronym("Python")}"')

# 7.23
def f_valid_password(password):
    if len(password) < 6:
        return False
    if len(password) != len(set(password)):
        return False
    return True

print(f'f("ax15") returns {f_valid_password("ax15")}')
print(f'f("book123") returns {f_valid_password("book123")}')
print(f'f("A2water3") returns {f_valid_password("A2water3")}')
print(f'f("qwerty") returns {f_valid_password("qwerty")}')
print(f'f("") returns {f_valid_password("")}')

# 7.24
def f_expression(expression):
    return eval(expression)

print(f'f("2+3") returns {f_expression("2+3")}')
print(f'f("3+8+1") returns {f_expression("3+8+1")}')
print(f'f("2+3-4+5-0") returns {f_expression("2+3-4+5-0")}')

# 7.25
def f_divisible_sum(x, y):
    total = 0
    for i in range(x, y + 1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            total += i
    return total

print(f'f(1,20) returns {f_divisible_sum(1, 20)}')
print(f'f(10,30) returns {f_divisible_sum(10, 30)}')

# 7.26
def f_dash_text(text):
    return "-".join(text)

print(f'f("Univesity") returns "{f_dash_text("Univesity")}"')
print(f'f("UE") returns "{f_dash_text("UE")}"')
print(f'f("x") returns "{f_dash_text("x")}"')
print(f'f("") returns "{f_dash_text("")}"')

# 7.27
def f_product_code(product_code):
    d1 = int(product_code[0])
    d2 = int(product_code[1])
    d3 = int(product_code[2])
    d4 = int(product_code[3])
    return (d1 + d2 + d3) % 7 == d4

print(f'f("1082") returns {f_product_code("1082")}')
print(f'f("2035") returns {f_product_code("2035")}')
print(f'f("1114") returns {f_product_code("1114")}')
print(f'f("7071") returns {f_product_code("7071")}')

# 7.28
def f_most_frequent_streak(dice):
    max_digit = dice[0]
    max_count = 0
    current_digit = dice[0]
    current_count = 0
    for char in dice:
        if char == current_digit:
            current_count += 1
        else:
            current_digit = char
            current_count = 1
        if current_count > max_count:
            max_count = current_count
            max_digit = char
    return int(max_digit)

print(f'f("5233165554211") returns {f_most_frequent_streak("5233165554211")}')
print(f'f("2133") returns {f_most_frequent_streak("2133")}')

# 7.29
def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n * factorial(n - 1)

print(f'Factorial of 5 is {factorial(5)}')

# 7.30
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

print(f'Sum of natural numbers in range <1,10> is {sum_natural(10)}')

# 7.31
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(f'5^3 is {power(5, 3)}')