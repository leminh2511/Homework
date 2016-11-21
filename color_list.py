color_list=["Blue","Red","Black","Pink","Brown","Yellow"]
print("My color list",color_list)
print("color_list at index 3:",color_list[3])
i=input("Enter a number from 0-5:")
if int(i)<6:
    print("Your color",color_list[int(i)])
else:
    print("Khong co trong color_list")

#In theo 2 cach
print(color_list)
i=0
for i in range(0,6):
    print(color_list[i])

#Index
x=input("What is your favorite color?")
if x in color_list:
    print("Your color is at index {0} in my list".format(color_list.index(x)))
else:
    print("Sorry, I could not find your color")

    
