def profit_rate_calculation(buy_price, sell_price):
    return 100 * ((sell_price - buy_price) / buy_price)


def profit_calculation(buy_price, sell_price, nb_currency):
    return nb_currency * (sell_price - buy_price)


def avrg_price_purchase(price_1, quantity_1, price_2, quantity_2):
    if price_1 == 0:
        avrg_buy_price = price_2 * (quantity_2 / (quantity_1 + quantity_2))
        print("Price 1 = 0")
    elif price_1 != 0:
        avrg_buy_price = price_1 * (quantity_1 / (quantity_1 + quantity_2)) + price_2 * (
                    quantity_2 / (quantity_1 + quantity_2))

    return avrg_buy_price


class Currency:
    def __init__(self, name):
        self.name = name
        self.transactions = []
        self.date = []
        self.side = []
        self.price = []
        self.quantityBuy = []
        self.currencySell = []
        self.quantitySell = []
        self.profit = []
        self.profitRate = []
        self.profitTotal = []
        self.balance = []
        self.average_buy_price = []
        self.transactionNumber = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        index = len(self.transactions) - 1

        self.date.append(transaction.date)
        self.side.append(transaction.side)
        self.price.append(transaction.quantitySell / transaction.quantityBuy)
        self.quantityBuy.append(transaction.quantityBuy)
        self.quantitySell.append(transaction.quantitySell)
        self.currencySell.append(transaction.currencySell)
        self.transactionNumber.append(transaction.transactionNumber)

        # Sell transaction
        if transaction.side == "SELL":
            # index = 0 is the first transaction of the currency table
            if index == 0:
                print("Error: It's impossible to sell a currency before buying it !")
                print("Transaction " + self.transactionNumber[index] + "not adding")
                return

            elif index > 0:
                self.balance.append(self.balance[index - 1] - self.quantityBuy[index])

                if self.balance[index] == 0:
                    # Sell 100%
                    self.average_buy_price.append(0)

                elif self.balance[index] != 0:
                    # Sell x %
                    self.average_buy_price.append(self.average_buy_price[index - 1])

                self.profitRate.append(profit_rate_calculation(self.average_buy_price[index - 1],
                                                               self.price[index]))
                self.profit.append(profit_calculation(self.average_buy_price[index - 1], self.price[index],
                                                      self.quantityBuy[index]))
                self.profitTotal.append(self.profitTotal[index - 1] + self.profit[index])

        # Buy transaction
        elif transaction.side == "BUY":
            self.profit.append(0)
            self.profitRate.append(0)
            if index == 0:
                self.average_buy_price.append(self.price[index])
                self.profitTotal.append(0)
                self.balance.append(self.quantityBuy[index])
            elif index > 0:
                self.profitTotal.append(self.profitTotal[index - 1])
                self.balance.append(self.balance[index - 1] + self.quantityBuy[index])
                self.average_buy_price.append(avrg_price_purchase(self.average_buy_price[index - 1],
                                                                  self.balance[index - 1], self.price[index],
                                                                  self.quantityBuy[index]))

    def print_overview(self):
        print(f'Date                  Side      Price {self.name}/{self.currencySell[0]}     Montant {self.name}      '
              f'Montant {self.currencySell[0]}      Gain %       Gain      Somme Gain    Balance {self.name}     '
              f'Avrg Buy Price')

        for index_transaction in range(len(self.transactions)):
            print(f'{self.date[index_transaction]:19}   {self.side[index_transaction]:4}    '
                  f'{round(self.price[index_transaction], 6):15}    {round(self.quantityBuy[index_transaction], 6):12}'
                  f'     {round(self.quantitySell[index_transaction], 6):12}   {round(self.profitRate[index_transaction], 2):7} '
                  f'{round(self.profit[index_transaction], 2):12}    {round(self.profitTotal[index_transaction], 2):12} '
                  f'  {round(self.balance[index_transaction], 6):12}    {self.average_buy_price[index_transaction]}')
