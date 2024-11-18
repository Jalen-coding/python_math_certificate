def truncate(n):
  multiplier=10
  return int(n*multiplier)/multiplier

def gettotals(categories):
  total=0
  breakdown=[]
  for category in categories:
    total+=category.get_withdrawls()
    breakdown.append(category.get_withdrawls())
  rounded=list(map(lambda x: truncate(x/total),breakdown))
  return rounded

def create_spend_chart(categories):
  res = 'Percentage spent by category\n'
  i=100
  totals=gettotals(categories)
  while i>=0:
      cat_spaces=' '
      for total in totals:
          if total * 100 >=i:
            cat_spaces+='o  '
          else:
            cat_spaces+='   '
      res+=str(i).rjust(3)+'|'+cat_spaces+('\n')
      i-=10

  dashes='-'+'---'*len(categories)
  names=[]
  x_axis=''
  for category in categories:
    names.append(category.name)

  maxi=max(names,key=len)
  
  for x in range(len(maxi)):
    namestr='     '
    for name in names:
      if x>=len(name):
        namestr+='   '
      else:
        namestr+=name[x]+'  '

    if(x != len(maxi)-1):
      namestr+='\n'

    x_axis+=namestr

  res+=dashes.rjust(len(dashes)+4)+'\n'+x_axis

  return res
  
    


class Category:
  def __init__(self, name):
    self.name=name
    self.ledger=list()

  def __str__(self):
    title=f"{self.name:*^30}\n"
    items =''
    total=0
    for item in self.ledger:
      items +=f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}"+'\n'
      total+=item['amount']

    output=title+items+'Total: '+str(total)
    return output

  def deposit(self,amount,description=''):
    '''
    A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should appened an object to the ledger list in the form of {"amount":amount,"description":description}   
    '''
    self.ledger.append({"amount":amount,"description":description})

  def withdraw(self,amount,description=''):
    '''
    A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothingnshouldnbe added to the ledger. This method should return True if the withdrawal took place, and False otherwise
    '''
    if(self.check_funds(amount)):
      self.ledger.append({"amount":-amount,"description":description})
      return True
    return False

  def get_balance(self):
    '''
    A get_balance method that returns the current balance of the budget category based on the deposits and withdraws that have occured
    '''
    total_cash=0
    for item in self.ledger:
      total_cash+=item['amount']
    
    return total_cash
    
  def transfer(self,amount,category):

    
    if(self.check_funds(amount)):
      self.withdraw(amount,'Transfer to '+category.name)
      category.deposit(amount,'Transfer from '+self.name)
      return True
    return False

  def check_funds(self,amount):
    if(self.get_balance()>=amount):
      return True
    return False
  def get_withdrawls(self):
    total=0
    for item in self.ledger:
      if item['amount']<0:
        total+=item['amount']
    return total
