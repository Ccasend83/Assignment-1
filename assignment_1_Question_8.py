import pandas as pd

initial_stored_column_data = {
"A": [1, 2, 2, 1],
"B": [3.1, 4.2, 1.5, 6.3],
"C": [800, 150, 400, 210]
}

new_panda_dataframe_for_storing_data = pd.DataFrame(initial_stored_column_data)
new_panda_dataframe_for_storing_data["D"] = (new_panda_dataframe_for_storing_data["C"] /
                                             new_panda_dataframe_for_storing_data["B"])
print(new_panda_dataframe_for_storing_data)