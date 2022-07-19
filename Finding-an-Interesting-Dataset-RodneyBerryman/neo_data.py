import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

neo_data = pandas.read_csv(
    "Finding-an-Interesting-Dataset-RodneyBerryman/neo.csv")

print(neo_data)