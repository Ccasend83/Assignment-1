import pandas as pd # we import the pandas library as pd so whenever we refer to it we use pd

initial_stored_column_data = { # this is our initial data given by the assignment page
"A": [1, 2, 2, 1],
"B": [3.1, 4.2, 1.5, 6.3],
"C": [800, 150, 400, 210]
}

new_panda_dataframe_for_storing_data = pd.DataFrame(initial_stored_column_data) # firstly we create the dataframe using our initial stored data
new_panda_dataframe_for_storing_data["D"] = (new_panda_dataframe_for_storing_data["C"] / # here we create a new row by dividing the contents of row "C" by the contents of row "B"
                                             new_panda_dataframe_for_storing_data["B"])
print(new_panda_dataframe_for_storing_data)
