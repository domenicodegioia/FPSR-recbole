import pandas as pd

dataset = 'facebook_books'
train_filename = 'train.tsv'
val_filename = 'val.tsv'
test_filename = 'test.tsv'

train = pd.read_csv('./Data/{0}/{1}'.format(dataset, train_filename),
                    sep='\t', header=None, names = ['user_id:token', 'item_id:token', 'rating:token'])
train = train.drop(train.columns[2], axis=1)

val = pd.read_csv('./Data/{0}/{1}'.format(dataset, val_filename),
                    sep='\t', header=None, names = ['user_id:token', 'item_id:token', 'rating:token'])
val = val.drop(val.columns[2], axis=1)

test = pd.read_csv('./Data/{0}/{1}'.format(dataset, test_filename),
                    sep='\t', header=None, names = ['user_id:token', 'item_id:token', 'rating:token'])
test = test.drop(test.columns[2], axis=1)

df = pd.concat([train, val, test], axis=0)#.sort_values(0).drop_duplicates()#.reset_index(drop=True)
df.to_csv('./Data/{0}/{0}.inter'.format(dataset), sep='\t', header=None, index=None)