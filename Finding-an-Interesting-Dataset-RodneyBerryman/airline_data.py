import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

airlines_data = pandas.read_csv(
    "Finding-an-Interesting-Dataset-RodneyBerryman/Airlines.csv")

print(airlines_data)