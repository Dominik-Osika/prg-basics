

# 1.3
speed_limit = 140
car_speed = int(input('Enter car speed (km/h): '))

if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')

# 1.4
account_balance = 500
total_payment = int(input('Enter total payment: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')

# 1.5
total_tasks = 20
tasks_ok = int(input('Enter number of correctly completed tasks: '))
test_passed = False

if tasks_ok >= total_tasks * 0.5:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')

# 1.6
number = int(input('Enter number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

# 1.7
basic_salary = 5000
total_salary = 0
bonus = 0.15
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')


# --- 2. Multiple Conditions ---

# 2.2
size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
elif size == 'XL':
    print('XL: Extra large size')
else:
    print('Incorrect symbol')

# 2.3
driving_mode = input('Enter driving mode (A/M/E):')
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7
elif driving_mode == 'M':
    fuel_consumption = 9
elif driving_mode == 'E':
    fuel_consumption = 6
else:
    fuel_consumption = 0

total_consumption = (distance / 100) * fuel_consumption
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')

# 2.4
number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2

print(f'{number1} {operator} {number2} = {result}')

# 2.5
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
else:
    quarter = 1

print(f'Month {month} is in quarter {quarter}')

# 2.6
number = int(input('Enter number: '))

if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    print('Number is 0')


# --- 3. Logical Operators ---

# 3.2
login = 'joe'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')

# 3.3
age = int(input('Enter your age: '))

if age < 18 or age >= 65:
    print('Discount is available')
else:
    print('No discount')

# 3.4
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')

# 3.5
month = int(input('Enter month number (1..12): '))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
else:
    days = 28

print(f'Month {month} has {days} days')

# 3.6
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day >= 1 and day <= 31:
        day_ok = True
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 1 and day <= 30:
        day_ok = True
elif month == 2:
    if day >= 1 and day <= 28:
        day_ok = True

message = f'Day {day} for the month {month}'
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is not correct')


# --- 4. Iteration Over a Sequence ---

# 4.3
for i in range(6):
    print('Practice makes perfect!')

# 4.4
university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' '

print(university)
print(university_expanded)

# 4.5
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    code = ord(char)
    code = code + 1
    new_char = chr(code)
    encrypted_text = encrypted_text + new_char

print(plain_text)
print(encrypted_text)

# 4.6
sum = 0

for i in range(5, 11):
    sum += i

print(f'Sum is {sum}')

# 4.7
sum = 0

for i in range(1, 11):
    if i % 2 != 0:
        continue
    sum += i

print('Sum of even numbers in the range <1,10> is ' + str(sum))

# 4.8
for i in range(1, 11):
    print(f'1/{i} = {1 / i}')


# --- 5. Conditional Iteration ---

# 5.2
count = 0
while count < 5:
    print(count)
    count += 1

# 5.3
name = ''

while name == '':
    name = input('Enter your name: ')

print(f'Hello {name}')

# 5.4
import random

number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

# 5.5
total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break
    total_sum += number
    count += 1

mean = total_sum / count if count > 0 else 0
print(f"The total sum of the numbers is: {total_sum}")
print(f"The arithmetic mean is: {mean}")

# 5.6
N = 10
sum_even = 0
i = 1

while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")

# 5.7
import time

seconds = int(input("Enter number of seconds to countdown: "))

while seconds > 0:
    if seconds == 5:
        print("five")
    elif seconds == 4:
        print("four")
    elif seconds == 3:
        print("three")
    elif seconds == 2:
        print("two")
    elif seconds == 1:
        print("one")
    else:
        print(seconds)
    time.sleep(1)
    seconds -= 1

print("Time's up!")

# 5.8
balance = 1000
pin = "1234"

attempts = 3
while attempts > 0:
    entered_pin = input("Enter 4-digit PIN: ")
    if entered_pin == pin and len(entered_pin) == 4 and entered_pin.isdigit():
        print("PIN correct.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}")

if attempts == 0:
    print("Card blocked.")
else:
    while True:
        print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Change PIN\n5. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            print(f"Balance: {balance}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            balance += amount
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
            else:
                print("Insufficient funds.")
        elif choice == '4':
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("PIN changed successfully.")
            else:
                print("Invalid PIN format.")
        elif choice == '5':
            break


# --- 6. Practice Makes Perfect ---

# 6.2
text = "The quick brown fox"
vowels = "aeiouAEIOU"
vowel_count = 0
i = 0

while i < len(text):
    if text[i] in vowels:
        vowel_count += 1
    i += 1

print(f"Vowel count: {vowel_count}")

# 6.3
light_switch1 = False
light_switch2 = False
bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2

print(f'Bulbs on: {bulbs_on}')

# 6.4
new_password = input('Enter new password: ')
if len(new_password) < 12:
    print('Password too short (min. 12 chars)')
else:
    print('Password is long enough')

# 6.5
temperature = 32
if temperature > 35:
    print("It is extremely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0:
    print("It is cold")
else:
    print("Warning, frost")

# 6.6
hours = int(input("Enter parking hours: "))

if hours >= 1 and hours <= 2:
    fee = 5
elif hours >= 3 and hours <= 6:
    fee = 15
else:
    fee = 20

print(f"Parking fee: {fee} PLN")

# 6.7
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 64:
    print("Adult")
else:
    print("Senior")

# 6.8
person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))
person2_name = input('Enter second person name: ')
person2_age = int(input('Enter second person age: '))

if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults')
else:
    print(f'Either {person1_name} or {person2_name} is not an adult')

# 6.9
name = input('Enter name: ')
if name.endswith('a') and name != 'Kuba':
    print(f'{name} -- Polish female name')

# 6.10
human_years = int(input("Enter the dog's age in human years: "))

if human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4

print(f"The dog's age in dog's years is {int(dog_years)} years.")

# 6.11
current_price = 140.00
previous_price = 200.00

reduction_percentage = ((previous_price - current_price) / previous_price) * 100

print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")

if reduction_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(reduction_percentage)}%")

# 6.12
quantity = int(input("Number of products purchased: "))
price = float(input("Product price: "))

if quantity > 2:
    total = 2 * price + (quantity - 2) * (price * 0.75)
else:
    total = quantity * price

print(f"Amount to pay: {total:.2f}")

# 6.13
car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')

# 6.14
facebook = True
twitter = False
instagram = True

count = 0
if facebook:
    count += 1
if twitter:
    count += 1
if instagram:
    count += 1

if count >= 2:
    print('You are a good influencer!')
else:
    print('You are not a good influencer.')

# 6.15
ean = input('Enter EAN-13 article number: ')

if len(ean) == 13 and ean.isdigit():
    print('Article number is correct')
    if ean.startswith('590'):
        print('Article manufactured in Poland')
else:
    print('Article number is incorrect')

# 6.16
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n): ')
extra_spin = input('Extra spin? (y/n): ')

if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20

if extra_rinse == 'y':
    total_washing_time += 15

if extra_spin == 'y':
    total_washing_time += 9

print(f'Total washing time: {total_washing_time} minutes')

# 6.17
time_24 = input('Enter time (24-hour format hh:mm): ')
parts = time_24.split(':')
hours = int(parts[0])
minutes = parts[1]

if hours == 0:
    time_12 = f"12:{minutes}am"
elif hours < 12:
    time_12 = f"{hours}:{minutes}am"
elif hours == 12:
    time_12 = f"12:{minutes}pm"
else:
    time_12 = f"{hours - 12}:{minutes}pm"

print(f'Time in 12-hour format: {time_12}')

# 6.18
x = int(input('Enter x: '))
y = int(input('Enter y: '))

if x == 0 and y == 0:
    print(f'Point P({x},{y}) is in the position (0,0)')
elif x == 0:
    print(f'Point P({x},{y}) is on the y-axis')
elif y == 0:
    print(f'Point P({x},{y}) is on the x-axis')
elif x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
else:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')

# 6.19
print("SURVEY")
q1 = input('Are you interested in computer science? (y/n): ') == 'y'
q2 = input('Do you like playing computer games? (y/n): ') == 'y'
q3 = input('Do you have an Instagram account? (y/n): ') == 'y'

print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if q1 else 'No'}")
print(f"Playing computer games: {'Yes' if q2 else 'No'}")
print(f"Has an Instagram account: {'Yes' if q3 else 'No'}")

# 6.20
decimal = int(input('Enter decimal number: '))
original = decimal
binary = ''

if decimal == 0:
    binary = '0'
else:
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

print(f'{original}(10) = {binary}(2)')

# 6.21
amount = int(input('Enter the amount in PLN: '))
original = amount

coins_5 = amount // 5
amount = amount % 5

coins_2 = amount // 2
amount = amount % 2

coins_1 = amount

print(f'The amount of PLN {original} in coins:')
print(f'5 PLN coins: {coins_5}')
print(f'2 PLN coins: {coins_2}')
print(f'1 PLN coins: {coins_1}')

# 6.22
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print('BINGO', end=' ')
    elif i % 3 == 0:
        print('THREE', end=' ')
    elif i % 5 == 0:
        print('FIVE', end=' ')
    else:
        print(i, end=' ')

# 6.23
number = int(input('Enter number: '))

for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')

# 6.24
for i in range(1, 6):
    print('* ' * i)
for i in range(4, 0, -1):
    print('* ' * i)

# 6.25
for i in range(1, 10):
    print(str(i) * i)

# 6.26
correct_pin = "0805"
attempts = 3

while attempts > 0:
    entered_pin = input('Enter the PIN code: ')
    if entered_pin == correct_pin:
        print('Correct PIN.')
        break
    else:
        attempts -= 1
        print('Incorrect...')

if attempts == 0:
    print('Sorry, your payment card has been blocked.')

# 6.27
i = 6
while i >= 0:
    j = 1
    while j <= 3:
        print(f'{i+j}', end=' ')
        j += 1
    print()
    i -= 3

# 6.28
n = 20
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

# 6.29
n = int(input('Enter N: '))
count = 0
current = 2

print('Prime numbers:', end=' ')
while count < n:
    is_prime = True
    for i in range(2, int(current**0.5) + 1):
        if current % i == 0:
            is_prime = False
            break
    if is_prime:
        print(current, end=' ')
        count += 1
    current += 1

# 6.30
for i in range(1, 8):
    for j in range(7):
        print(i + j * 7, end='\t')
    print()

# 6.31
import random

for _ in range(20):
    print(random.randint(5, 10), end=' ')