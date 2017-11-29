
The first function ("checkout.py") implements the first bullet point, which is to code the respective function which calculates the total cost for the PoS supermarket problem. It perfomes "extremes" checks as well, for empty inputs, negative costs and items in product list which do not have associated cost in the Cost dictionary error detection.

The secound function ("checkout_test.py") adds sanity checking (to the extend possible) for the first function, that is, correctly verify proper cost calculation for each respective item separately and flagging out the case where a product has no associated offer (simply by checking that the total cost is just a mere multiplication of the respective price by the number of items listed).

