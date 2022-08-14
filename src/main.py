def isDivisible(number, divisor):
    return (divisor != 0 and number % divisor == 0)


print("Enter Number: ")
num = input()

check = True
print("Output: ")
for digit in range(0, len(num)):
    if isDivisible(int(num), int(num[digit])) != True:
        check = False

if check == False:
    print("No")
else:
    print("Yes")