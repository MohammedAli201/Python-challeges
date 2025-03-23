age = int(input("Enter your age: "))

print("Your entered age is : ", age)

if age < 13:
    print("Recommended: Animated Movies")
if age < 18:
    print("Recommended: Teen Movies")
else :
    print("Recommended: Action or Drama Movies")