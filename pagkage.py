
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
import calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Choose operation: +  -  *  /")
op = input("Enter operation: ")

if op == "+":
    print("Result:", calculator.add(a, b))
elif op == "-":
    print("Result:", calculator.subtract(a, b))
elif op == "*":
    print("Result:", calculator.multiply(a, b))
elif op == "/":
    print("Result:", calculator.divide(a, b))
else:
    print("Invalid operation")
import student

marks = [85, 90, 78, 88, 95]
total = student.total_marks(marks)
percent = student.percentage(marks, 100)
grade = student.grade(percent)

print("Total marks:", total)
print("Percentage:", percent)
print("Grade:", grade)
def total_marks(marks_list):
    return sum(marks_list)

def percentage(marks_list, max_marks_each):
    total = total_marks(marks_list)
    max_total = max_marks_each * len(marks_list)
    return (total / max_total) * 100

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "Fail"
import number_utils

n = int(input("Enter a number: "))

print("Prime:", number_utils.is_prime(n))
print("Palindrome:", number_utils.is_palindrome(n))
print("Armstrong:", number_utils.is_armstrong(n))
print("Perfect:", number_utils.is_perfect(n))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
import string_utils

s = input("Enter a string: ")

print("Vowel count:", string_utils.count_vowels(s))
print("Reversed:", string_utils.reverse_string(s))
print("Palindrome:", string_utils.is_palindrome(s))
print("Word count:", string_utils.count_words(s))
print("Without spaces:", string_utils.remove_spaces(s))
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_words(s):
    return len(s.split())

def remove_spaces(s):
    return s.replace(" ", "")

import salary

basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))

gross = salary.gross_salary(basic, allowances)
ded = salary.deductions(gross)
net = salary.net_salary(basic, allowances)

print("Gross salary:", gross)
print("Deductions:", ded)
print("Net salary:", net)
   def gross_salary(basic, allowances):
    return basic + allowances

def deductions(gross, deduction_rate=0.1):
    return gross * deduction_rate

def net_salary(basic, allowances, deduction_rate=0.1):
    gross = gross_salary(basic, allowances)
    ded = deductions(gross, deduction_rate)
    return gross - ded
import recursive_utils

n = int(input("Enter a number: "))

print("Factorial:", recursive_utils.factorial(n))
print("Fibonacci series:", recursive_utils.fibonacci_series(n))
print("Sum of digits:", recursive_utils.sum_of_digits(n))
print("Binary form:", recursive_utils.to_binary(n))
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci_series(n):
    series = []
    def fib(k):
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)
    for i in range(n):
        series.append(fib(i))
    return series

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)
