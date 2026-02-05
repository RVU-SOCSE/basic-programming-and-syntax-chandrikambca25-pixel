Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#USN:1RUA25BCA0019 NAME: CHANDRIKA M
#Program to find a simple calculator

#match case for operations

num1=float(input("Enetr first number:"))
Enetr first number:2.6
num2=float(input("Enter second number:"))
Enter second number:3.4

print ("Choose operation:")
Choose operation:
print("+ Addition")
+ Addition
print("- Subtraction")
- Subtraction
print("* Multiplication")
* Multiplication
print("/ Division")
/ Division
print("% Modulus")
% Modulus

match choice:
    case "+":
        print("Result=",num1+num2)

        
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    match choice:
NameError: name 'choice' is not defined

================ RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ===============
Enetr first number:3.4
Enter second number:2.6
Choose operation:
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
Traceback (most recent call last):
  File "C:/Users/RVUW268/Desktop/pythonlab3.py", line 15, in <module>
    match choice:
NameError: name 'choice' is not defined

================ RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ===============
Enetr first number:3.4
Enter second number:2.6
Choose operation:
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
Traceback (most recent call last):
  File "C:/Users/RVUW268/Desktop/pythonlab3.py", line 13, in <module>
    match choice:
NameError: name 'choice' is not defined

================ RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ===============
Enetr first number:3.4
Enter second number:3.6
Choose operation:
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
+
Result= 7.0

================ RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ===============
Enetr first number:4.6
Enter second number:5.6
Choose operation:
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
-
Result= -1.0

================ RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ===============
Enetr first number:4.6
Enter second number:5.6
Choose operation:
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
*
Result= 25.759999999999998

================ RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ===============
Enetr first number:4.6
Enter second number:5.6
Choose operation:
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
/
Result= 0.8214285714285714

================ RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ===============
Enetr first number:4.6
Enter second number:5.6
Choose operation:
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
%
Result= 4.6
#program to finfd temperature conversion
#USN:1RUA25BCA0019  NAME:CHANDRIKA M
>>> 
==================================================== RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ====================================================
Traceback (most recent call last):
  File "C:/Users/RVUW268/Desktop/pythonlab3.py", line 1, in <module>
    t=float("Enter Temperatue:")
ValueError: could not convert string to float: 'Enter Temperatue:'
>>> 
==================================================== RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ====================================================
Enter Temperatue:32
Convert to(F/C/K):F
Result= 89.6
>>> 
==================================================== RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ====================================================
Enter Temperatue:-7
Convert to(F/C/K):
Traceback (most recent call last):
  File "C:/Users/RVUW268/Desktop/pythonlab3.py", line 2, in <module>
    c=input("Convert to(F/C/K):")
KeyboardInterrupt
>>> 
==================================================== RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ====================================================
Enter Temperatue:-7
Convert to(F/C/K):C
Result= -21.666666666666668
>>> 
==================================================== RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ====================================================
Enter Temperatue:60
Convert to(F/C/K):K
Result= 333.15
>>> #program to find Minmum and Maximum value
... #USN:1RUA25BCA0019  NAME:CHANDRIKA M
>>> 
>>> 
==================================================== RESTART: C:/Users/RVUW268/Desktop/pythonlab3.py ====================================================
enter the first number:6
enter the second number:8
enter the third number:7
maximum value: 8
minimum value: 6
