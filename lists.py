def nested_sum(t,x):
    for num in t:
        if isinstance(num,list):
            x += nested_sum(num,0)
        else:
            x += num
    return x
