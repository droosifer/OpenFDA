import json
import pandas as pd


data = json.load(open('/home/drew/Documents/open_fda_project/py_charm_project/files/json_files2/files/test.json'))


new_data = pd.json_normalize(data)


works_data = pd.json_normalize(data, ['drug', 'active_ingredients'])


works_data.to_csv('/home/drew/Documents/open_fda_project/py_charm_project/files/json_files2/files/conversion_test.csv', index=False)


# def flatten_nested_json_df(df):
#
#     df = df.reset_index()
#
#     print(f"original shape: {df.shape}")
#     print(f"original columns: {df.columns}")
#
#     # search for columns to explode/flatten
#
#     s = (df.applymap(type) == list).all()
#     list_columns = s[s].index.tolist()
#
#     s = (df.applymap(type) == dict).all()
#     dict_columns = s[s].index.tolist()
#
#     print(f"lists: {list_columns}, dicts: {dict_columns}")
#     while len(list_columns) > 0 or len(dict_columns) > 0:
#         new_columns = []
#
#         for col in dict_columns:
#             print(f"flattening: {col}")
#             # explode dictionaries horizontally, adding new columns
#             horiz_exploded = pd.json_normalize(df[col]).add_prefix(f'{col}.')
#             horiz_exploded.index = df.index
#             df = pd.concat([df, horiz_exploded], axis=1).drop(columns=[col])
#             new_columns.extend(horiz_exploded.columns) # inplace
#
#         for col in list_columns:
#             print(f"exploding: {col}")
#             # explode lists vertically, adding new columns
#             df = df.drop(columns=[col]).join(df[col].explode().to_frame())
#             new_columns.append(col)
#
#         # check if there are still dict o list fields to flatten
#         s = (df[new_columns].applymap(type) == list).all()
#         list_columns = s[s].index.tolist()
#
#         s = (df[new_columns].applymap(type) == dict).all()
#         dict_columns = s[s].index.tolist()
#
#         print(f"lists: {list_columns}, dicts: {dict_columns}")
#
#     print(f"final shape: {df.shape}")
#     print(f"final columns: {df.columns}")
#     return df


# un_nested_df = flatten_nested_json_df(new_data)

