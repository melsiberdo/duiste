import pandas as pd

# Assuming your dataset is stored in a variable called df
df['comment_disabled'] = None  # or you can set it to True or False based on your requirements

# If you want to set the entire column to a specific value, you can do so using:
# df['comment_disabled'] = True  # or False

# If you have specific conditions to determine the value of the new column, you can use:
# df['comment_disabled'] = df['some_other_column'] > 10
