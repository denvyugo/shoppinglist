__Shopping List__

This a command line utility that can check total cost of shopping list what you going to do by a statistic information of previous shopping.

Every day we do shopping. If you wann't to keep in memory price for every good in your cart, you may do a list in such format in csv file:

`number, date, good, cost`

So than you going to shopping you may fill a list and check how much it will cost with this command:

`shoppinglist.py -g "good1" "good2"`

There a good1, good2 are names of good what you going to buy.

Use help:
`shoppinglist.py -h`

    usage: shoppinglist.py [-h] [-u] [-b] [-g [GOODS [GOODS ...]]] [-q QUANTILE]
    
    An utility for working with shopping list
    
    optional arguments:
    -h, --help            show this help message and exit
    -u, --update          update data file from upload from shopping list
    -b, --buyings         show buyings from shopping list
    -g [GOODS [GOODS ...]], --goods [GOODS [GOODS ...]]
                        shopping list of goods thrue whitespace
    -q QUANTILE, --quantile QUANTILE
                        quantile factor (float) for probability of maximum price of good


