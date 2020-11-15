**7 kyu**
# Jumping Number (Special Numbers Series #4)

Jumping number is the number that **all** adjacent digits in it differ by 1.

# Task
Given a number, find if it is jumping or not.

**Notes:**
- Number passed is always positive .
- Return the result as `string` .
- The difference between `9` and `0` is *not* considered as `1` .
- All single digit numbers are considered as jumping numbers.

# Examples
```
jumpingNumber(9) ==> return "Jumping!!"
```
- It's single-digit number

```
jumpingNumber(79) ==> return "Not!!"
jumpingNumber(556847) ==> return "Not!!"
```
- Adjacent digits don't differ by 1

```
jumpingNumber(23) ==> return "Jumping!!"
jumpingNumber(4343456) ==> return "Jumping!!"
```
- Adjacent digits differ by 1
