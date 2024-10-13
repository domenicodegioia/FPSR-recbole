import pandas as pd

dataset = 'ml-1m'
train_filename = 'train_sparse.csv'
test_filename = 'test_sparse.csv'

rows, cols = [], []
with open('./Data/{0}/{1}'.format(dataset, train_filename), 'r') as f:
    for line in f:
        all_elements = line.split(',')
        if '\n' not in all_elements:
            for el in all_elements[1:]:
                rows.append(int(all_elements[0]))
                cols.append(int(el))

train = pd.concat([pd.Series(rows), pd.Series(cols)], axis=1)

rows, cols = [], []
with open('./Data/{0}/{1}'.format(dataset, test_filename), 'r') as f:
    for line in f:
        all_elements = line.split(',')
        if '\n' not in all_elements:
            for el in all_elements[1:]:
                rows.append(int(all_elements[0]))
                cols.append(int(el))

test = pd.concat([pd.Series(rows), pd.Series(cols)], axis=1)

df = pd.concat([train, test], axis=0).sort_values(0).drop_duplicates().reset_index(drop=True)
df.to_csv('./Data/{0}/ml-1m.inter'.format(dataset), sep='\t', header=None, index=None)