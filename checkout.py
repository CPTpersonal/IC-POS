
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
