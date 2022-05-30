#binary search algorithm

def binary_search(num_list, item):
    first = 0
    last = len(num_list)-1
    while first <= last:
        i = (first + last)/ 2
        if num_list [i] == item:
            return 'number was found at position ' .format(item=item,i=i)
        elif num_list[i] > item:
            last = i - 1
        elif num_list < item:
            first = i + 1
        else:
            return ' num was not found in the list '.format(item=item)


