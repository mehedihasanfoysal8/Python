def sum_all(*args):
    
    for i in args:
        print("Inner loop", i)

    return sum(args)

print(sum_all(2, 4, 6, 8))