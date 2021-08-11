def remove_duplicates(some_list):
    without_duplicates=[]
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def remove_duplicates_with_sets(some_list):
    new_set=set(some_list)
    list_without_duplicates=list(new_set)
    return list_without_duplicates

def run():
    random_list=[1,1,2,2,4]
    print(remove_duplicates_with_sets(random_list))



if __name__=='__main__':
    run()