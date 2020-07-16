def gen_open_goods():
    """open file goods.csv for read by row"""
    with open('goods.csv', 'r') as file:
        for row in file:
            yield row

def load_goods():
    """load data from goods.cvs
    (Window, Excel, Russian format - semicolon delimeters)
    to buyings.csv (uft-8, comma separated)"""
    goods = gen_open_goods()
    add_head = True
    with open('buyings.csv', 'w', encoding='utf-8') as buyings:
        for good in goods:
            if add_head:
                new_line = 'number,date,good,quantity,unit,price,cost,remark'
                add_head = False
            else:
                new_line = good.replace('р. ', '').replace(',', '.')\
                           .replace(';', ',')
            buyings.write(new_line)
    
if __name__ == '__main__':
    load_goods()

