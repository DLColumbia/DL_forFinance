# Deep Learning for Finance - Deep Portfolio

This git repository is based on the work of J.Heaton, N.Polson and J.Witte and their article **Deep Learning for Finance: Deep Portfolios**.  This paper let us explore the use of deep learning  models  for  problems  in  financial  prediction  and  classification.   Our  goal  is to  show  how  applying  deep  learning  methods  to  these  problems  can  produce  better outcomes than standard methods in finance or in Machine Learning

In this repository, we only present the code related to our work with the IBB index. To obtain the same results with another index (such as the S&P500 as presented in our paper), one would simply use the appropriate list of stocks data (can be easily find using the Yahoo finance API and the code IBB-Data-Extraction.ipynb by modifying "IBB" in the code by the name of the index one wants to replicate).

## What is included in this repos ?
We included in our github repository the following files:
1. **IBB_holdings.csv**: a csv file containing the list of tickers for the IBB index
2. **IBB-Data-Extraction.ipynb**: a jupyter notebook to automatically gather the data using Yahoo Finance API
3. **IBB-Replication.ipynb**: a jupyter notebook explaining step by step the Deep Learning method we used to replicate the IBB
4. **Deep Learning for Finance - Deep Portfolio.pdf**: a paper presenting the results obtained during the semester
5. **DeepLearning_presentation.pdf**: presentation we made in front of the class
6. **Backtest_Quantopian.py**: Backtest of our strategy on S&P and IBB (Precaution: do not try to run it. It will only work on Quantopian: cut and paste the code on an empty Quantopian algorithm.




## Written by 
T.Becker, M.Bergerot, P.de Kerdrel, A.Mascia, N.Tachet
## Under the supervision of 
**Professor**:  Ali Hirsa
**Teacher Assistant**:  Francois Fagan
