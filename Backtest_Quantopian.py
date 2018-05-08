# Algorithm API imports
import quantopian.algorithm as algo
import pandas as pd
import datetime

# PLEASE CUT AND PASTE ALL THE DOCUMENT ON AN EMPTY QUANTOPIAN ALGORITHM
# THIS CODE WON'T WORK ON ANY USUAL PYTHON PLATFORM

#==============================================================================

# SET A INVESTMENT SIZE OF 100K$

# IN RANGE: 05/05/2015 to 05/02/2017
# OUT RANGE: 06/03/2017 to 12/28/2017

# CHOOSE ONE OF THE FOLLOWING:
# IBB OUT SAMPLE:
# https://dl.dropboxusercontent.com/s/lagetj445dxzpma/Weigths.csv?dl=0
# SP IN SAMPLE:
# https://dl.dropboxusercontent.com/s/numgde3pubor5yj/Weigths_in.csv?dl=0
# SP OUT SAMPLE:
# https://dl.dropboxusercontent.com/s/ozf1vuoopcvxxup/Weigths_out.csv?dl=0

URL = 'https://dl.dropboxusercontent.com/s/ozf1vuoopcvxxup/Weigths_out.csv?dl=0'

#==============================================================================

def preview(df):
    log.info(' \n %s ' % df.head())
    return df

#==============================================================================

def initialize(context):

    fetch_csv(URL,
              pre_func=preview,
              date_column='date',
              date_format='%Y-%m-%d'
              )

    # Set the benchmark to the IBB - 22445
    # set_benchmark(sid(22445))
    # Set the benchmark to the SPY - 8554
    set_benchmark(sid(8554))

    # Rebalance every day, at end of day to account for forward bias
    algo.schedule_function(
        rebalance,
        algo.date_rules.month_start(),
        algo.time_rules.market_open(hours=0,
                                   minutes=20),
    )

#==============================================================================

def before_trading_start(context, data):
    # Get the weights that will have to be traded
    context.weights = data.current(data.fetcher_assets, 'weight')

    # Update the universe
    context.assets = context.weights.index

#==============================================================================

def rebalance(context, data):

    for stock in context.weights.index:
        if stock not in context.portfolio.positions:
            if data.can_trade(stock) and data.current(stock, 'price') != None:
                # We're dealing with exotic ones... Check if data available
                log.info( 'long {A}; weight {B}; price {C}'.format(
                        A=stock,
                        B=context.weights[stock],
                        C=data.current(stock, 'price')))
                order_target_percent(stock, context.weights[stock])
