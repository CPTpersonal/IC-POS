def checkout_test(Products, Cost):
    """assert sanity of the checkout function above"""
    flag = True
    total_cost_no_offers = 0 # sanity check total cost to evaluate case where no offer is active
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

    # assess if no offer is active
    for key in Cost:
        occ = Products.count(key)
        total_cost_no_offers += occ * Cost[key]
    if total_cost_no_offers == checkout(Products, Cost):
        print("Calculations do not take into account any offers!")
        flag = False
    
    print("***********************************************")
    print("Total assesement of sanity checks: " + str(flag))
    print("***********************************************")
    return flag
    

checkout_test(["A"], {"A": 50})
checkout_test(['B', 'A', 'B', 'P', 'B'], {'A': 25, 'B': 40, 'P': 30})
checkout_test(['P', 'P', 'P', 'P', 'P'], {'A': 25, 'B': 40, 'P': 30})
