import pandas as pd
    

def load_table():
    """load buyings data from csv file"""
    buyings = pd.read_csv('buyings.csv', index_col='number')
    return buyings


def buying_list(buyings, buying_goods, factor=0.8):
    """take a 80% probability cost for goods in buying list"""
    buying = {}
    for good in buying_goods:
        good_frame = buyings[buyings['good'] == good]
        buying[good] = good_frame['cost'].quantile(factor)
    return buying
