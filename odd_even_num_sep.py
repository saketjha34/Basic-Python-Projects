

def odd_even_sep(lower_limit, upper_limit):
    odd_list = []
    even_list = []

    for i in range(lower_limit, upper_limit+1):
        if i == 0:
            continue
        if i % 2== 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print(f"Even Numbers are : {even_list}" )
    print(f"odd Numbers are : {odd_list}" )


if __name__ == '__main__':
    lower_limit = int(input("Enter The Lower Limit :"))
    upper_limit = int(input("Enter The upper Limit :"))
    odd_even_sep(lower_limit,upper_limit)