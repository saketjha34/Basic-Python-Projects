
odd_list = []
even_list = []
lower_limit = int(input("Enter The Lower Limit :"))
upper_limit = int(input("Enter The upper Limit :"))

for i in range(lower_limit, upper_limit+1):
    if i == 0:
        continue
    if i % 2== 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"Even Numbers are : {even_list}" )
print(f"odd Numbers are : {odd_list}" )
