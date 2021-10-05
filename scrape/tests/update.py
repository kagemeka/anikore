import pandas as pd 


columns = ['a', 'b']

a = pd.DataFrame({
  'a': [1, 2, 6, 8],
  'b': [2, 3, 4, 5],
})

b = pd.DataFrame({
  'a': [1, 6, 3],
  'b': [5, 3, 4],
})


# a.set_index('a', inplace=True)
# b.set_index('a', inplace=True)

c = pd.concat((a, b), ignore_index=True)
c.drop_duplicates(subset=['a'], keep='last', inplace=True)

print(c)