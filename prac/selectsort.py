def selectsort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        minimum = iter

        for cur in range(iter+1, len(lst)):
            if lst[cur] < lst[minimum]:
                minimum = cur

            if minimum != iter:
                lst[minimum], lst[iter] = lst[iter], lst[minimum]

    return lst
