import datetime
class Item:
  shippingWeight : str
  description : str
  def __init__(self, shippingWeight, description):
    self.shippingWeight = shippingWeight
    self.description = description
  def getPriceForQuantity(self):
    pass
  def getTax(self):
    pass
  def inStock(self):
    pass

class OrderDetails():
  quantity: str
  taxStatus: str
  item : Item
  def __init__(self,quantity, taxStatus):
    self.quantity = quantity
    self.taxStatus = taxStatus
  def calcSubTotal(self):
    pass
  def calcWeight(self):
    pass
  def calcTax(self):
    pass

class Payment:
  amount : str

  def __init__(self) -> None:
    super().__init__()
    self.amount = amount


class Cash(Payment):
  cashTendered : str
  def __init__(self, amount, cashTendered):
    Payment.__init__(self,amount)
    self.cashTendered = cashTendered


class Check(Payment):
  name:str
  bankid:str
  def __init__(self, amount, name, bankId):
    Payment.__init__(self,amount)
    self.name = name
    self.bankId = bankId
  def authorize(self):
    pass
  def payMoney(self):
    pass

class Credit(Payment):
  number:str
  type:str
  expDate:str
  def __init__(self, amount, number, type, expDate):
    Payment.__init__(self,amount)
    self.number = number
    self.type = type
    self.expDate = expDate
  def authorize(self):
    pass
  def payMoney(self):
    pass
class Order():
  orderdetail : list[OrderDetails]
  payment : list[Cash, Check, Credit]
  date : datetime
  status : str
  def __init__(self, date, status):

    super().__init__()
    self.date = date
    self.status = status
  def calcSubTotal(self):
    pass
  def calcTax(self):
    pass
  def calcTotal(self):
    pass
  def calcTotalWeight(self):
    pass

class Customer:
  name : str
  address: str
  orders: list[Order]
  def __init__(self, name, address):
    self.name = name
    self.address = address

