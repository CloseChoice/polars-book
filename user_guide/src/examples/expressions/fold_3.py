import polars as pl

df = pl.DataFrame({"a": ["a", "b", "c"], "b": [1, 2, 3]})

out = df[[pl.concat_str(["a", "b"])]]
