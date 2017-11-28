
def  checkout(Products, Cost):
    """This function answers queries on products and their total cost"""
    total_cost = 0 # initializing total cost
    # first do a sanity check on inputs
    if type(Products) is not list or type(Cost) is not dict:
        print("Error: The products must be in a list and the costs in a dictionary. Exiting...")
    else:
        # checking if inputs are non-empty
        if Products == [] or Cost == {}:
            print("Error: One of the input lists is empty. Exiting...")
        # checking if each product entry has an associated cost    
        for product in set(Products): # using set to reduce number of checks for efficiency
            if product not in Cost.keys():
                print("Error: product {:s} has no associated cost entry. Exiting...".format(product))
        else:
            # executing what the function is supposed to implement now:
            for key in Cost:
                occ = Products.count(key) # find the occurencies of each key
                if key == 'A':
                    total_cost += int(occ / 3)*(Cost[key]*2) + (occ % 3)*Cost[key]
                elif key == 'B':
                        total_cost += int(occ / 3)*100 + (occ % 3)*Cost[key]
                elif key == 'P':
                    total_cost += occ*Cost[key]
                    
    print("Total associated cost based on offers is: {:f} pence".format(total_cost))
    return total_cost
        
checkout(['B', 'A', 'B', 'P', 'B'], {'A': 25, 'B': 40, 'P': 30})
checkout(['B', 'B', 'B', 'B', 'B'], {'A': 25, 'B': 40, 'P': 30})
checkout(['A', 'A', 'A', 'A', 'A'], {'A': 25, 'B': 40, 'P': 30})
checkout(['P', 'P', 'P', 'P', 'P'], {'A': 25, 'B': 40, 'P': 30})

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
