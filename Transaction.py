class Transactions:
    def __init__(self, currencyBuy, quantityBuy, currencySell, quantitySell, side, date, transactionNumber):
        self.currencyBuy = currencyBuy
        self.currencySell = currencySell
        self.side = side
        self.date = date
        self.quantityBuy = quantityBuy
        self.quantitySell = quantitySell
        self.transactionNumber = transactionNumber

    def get_currencyBuy(self):
        return self.currencyBuy

    def get_quantityBuy(self):
        return self.quantityBuy

    def get_currencySell(self):
        return self.currencySell

    def get_quantitySell(self):
        return self.quantitySell

    def get_side(self):
        return self.side

    def get_date(self):
        return self.date

    def get_transactionNumber(self):
        return self.transactionNumber