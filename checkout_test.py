def checkout_test(Products, Cost):
    """assert sanity of the checkout function above"""
    flag = True
    print("-------------Sanity Checking-------------")
    # check if the cost is correctly calculated for each singular appearance of each product
    # that is if : checkout(['B'], {'B': 40}) then total cost should be equal to the only cost defined
    for item in set(Products): # only check the unique elements
        cost = checkout([item], {item : Cost[item]})
        if cost != Cost[item]:
            print("Error: the cost of item {} is not correctly calculated!".format(item))
            flag = False
        else:
            print("Checking cost for item {}:".format(item) + " " + str(cost))

            
    # check that empty lists, or one of the two, return zero cost
    cost = checkout([], {})
    if cost != 0:
        print("Error: the cost of empty inputs should be zero!")
        flag = False
    else:
        print("Cost of empty inputs is :" + str(cost))
    
    print("***********************************************")
    print("Total assesement of sanity checks: " + str(flag))
    print("***********************************************")
    return flag
    

checkout_test(["A"], {"A": 0})
checkout_test(['B', 'A', 'B', 'P', 'B'], {'A': 25, 'B': 40, 'P': 30})
checkout_test(['P', 'P', 'P', 'P', 'P'], {'A': 25, 'B': 40, 'P': 30})
