import argparse


def parse():
    """parse arguments of command string,
    return dict with argument: value"""
    parser = argparse.ArgumentParser(
        description='An utility for working with shopping list')
    parser.add_argument('-u', '--update', action='store_true',
                        help='update data file from upload from shopping list')
    parser.add_argument('-b', '--buyings', action='store_true',
                        help='show buyings from shopping list')
    parser.add_argument('-g', '--goods', nargs='*', type=str,
                        help='shopping list of goods thrue whitespace')
    parser.add_argument('-q', '--quantile', type=float, default=0.8,
                        help='quantile factor (float) for probability \
                                of maximum price of good')

    args = parser.parse_args()
    return {'update': args.update,
            'buyings': args.buyings,
            'goods': args.goods,
            'quantile': args.quantile}


def print_check(buying_list):
    """print check for buying list"""
    total = 0
    print('Check for shopping')
    print('-' * 20)
    for good, cost in buying_list.items():
        round_cost = round(cost, 2)
        total += round_cost
        print(good, round_cost)
    print('-' * 20)
    print('Total:', total)


def update_goods():
    """update buyings.cvs from goods.csv uploads from excell"""
    import goods
    goods.load_goods()


def work_foods(arguments):
    """working with buyings commands"""
    import buyings
    buyings_table = buyings.load_table()
    if arguments['buyings']:
        print(set(buyings_table['good']))
    if arguments['goods']:
        buying_list = buyings.buying_list(buyings_table,
                                        arguments['goods'],
                                        factor=arguments['quantile'])
        print_check(buying_list)


def main():
    arguments = parse()
    if arguments['update']:
        update_goods()
    if arguments['buyings'] or arguments['goods']:
        print('Loading data. Please wait...')
        work_foods(arguments)


if __name__ == '__main__':
    main()
    
