'''
Created on 09/18/2019

@author: David Ulevitch
'''
# standard libraries
from datetime import timedelta, datetime
import os

# third-party libraries
from matplotlib.pyplot import show

# own libraries
from FinancialLife.financing import accounts as a
from FinancialLife.reports import html

def example2():
    # create a private bank account and a loan
    account = a.BankAccount(amount = 0, interest = 0.001, name = 'Checking')
    wealthfront = a.BankAccount(amount = 260000, interest = 0.0232, name = 'Savings')
    l_1stanyan = a.Loan(amount = 1338750, interest = 0.03125, name = 'Refinanced 1 Stanyan')
    l_80ptl = a.Loan(amount = 794750, interest = 0.03125, name = 'Refinanced 80 PTL')
    l_1001genter = a.Loan(amount = 1360000, interest = 0.03, name = 'Refinanced 1001 Genter')

    # add these accounts to the simulation
    simulation = a.Simulation(account, wealthfront, l_1stanyan, l_80ptl, l_1001genter)

    # describe single or regular payments between accounts. note, that
    # a string can be used for external accounts that you don't want to model.
    # also note the lambda function for the payments to the loan.
    simulation.add_regular('Income', account, 40000, interval = 'monthly', date_start=datetime(2019,9,1))
    simulation.add_regular('Income', account, 40000, interval = 'monthly', date_start=datetime(2019,9,15))
    simulation.add_regular(account, wealthfront, 25000, interval = 'monthly')
    simulation.add_regular(account, l_1stanyan, lambda: min(5735, -l_1stanyan.account), interval = 'monthly')
    simulation.add_regular(account, l_80ptl, lambda: min(3405, -l_80ptl.account), interval = 'monthly')
    simulation.add_regular(account, l_1001genter, lambda: min(5734, -l_1001genter.account), interval = 'monthly')
    

    # simulate for ten years
    simulation.simulate(delta = timedelta(days=365*30))
    # plot the data
    simulation.plt_summary()

    # print reports summarized in years
    print(account.report.yearly().as_df())
    #print(1loan.report.yearly().as_df())
    
    # analyze data
    print("Bank account: %.2f" % (account.account + wealthfront.account))

    cwd = os.path.dirname(os.path.realpath(__file__))
    result_folder = cwd + '/example2'

    html.report(simulation, style="standard", output_dir = result_folder)
    show()

def example3():
    account = a.BankAccount(amount = 50000, interest = 0.001, name = 'Checking')
    savings = a.BankAccount(amount = 5000000, interest = 0.022, name = 'Savings')
    loan = a.Loan(amount = 4000000, interest = 0.0325, name = 'Refinanced Cash')

    simulation = a.Simulation(account, savings, loan, name = 'Scenario')
    simulation.add_regular(from_acc = 'Income',
                           to_acc = account,
                           payment = 40000,
                           interval = 'monthly',
                           date_start = datetime(2019,1,1),
                           day = 1,
                           name = 'Income')
    simulation.add_regular(from_acc = 'Income',
                           to_acc = account,
                           payment = 40000,
                           interval = 'monthly',
                           date_start = datetime(2019,1,1),
                           day = 15,
                           name = 'Income')

    simulation.add_regular(from_acc = account,
                           to_acc = savings,
                           payment = 20000,
                           interval = 'monthly',
                           date_start = datetime(2019,1,1),
                           day = 1,
                           name = 'Savings')

    simulation.add_regular(from_acc = account,
                           to_acc= loan,
                           payment = 40000,
                           interval = 'monthly',
                           date_start = datetime(2019,1,1),
                           day = 1,
                           name = 'Debts',
                           fixed = False,
                           date_stop = lambda cdate: loan.is_finished())

    simulation.simulate(delta = timedelta(days=365*3))

    simulation.plt_summary()
    show()

    print(account.report)
    print(loan.report)

if __name__ == '__main__':
    example2()

