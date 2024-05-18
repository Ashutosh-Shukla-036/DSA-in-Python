def main():

    arr = list(map(int,input("Enter array element:").split()))

    freq_list = {}

    for i in arr:
        if i in freq_list:
            freq_list[i] += 1
        else:
            freq_list[i] = 1

    q = int(input("Enter number of query:"))

    for _ in range(q):
        number = int(input("Enter query number:"))
        print(freq_list.get(number,0))

if __name__ == "__main__":
    main()