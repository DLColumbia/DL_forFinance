# Deep Learning for Finance - Deep Portfolio

#### Written by 
T.Becker, M.Bergerot, P.de Kerdrel, A.Mascia, N.Tachet
#### Under the supervision of 
**Professor**:  Ali Hirsa
**Teacher Assistant**:  Francois Fagan

This git repository is based on the work of J.Heaton, N.Polson and J.Witte and their articleDeep Learning for Finance: Deep Portfolios.  This paper let us explore the use of deeplearning  models  for  problems  in  financial  prediction  and  classification.   Our  goal  is to  show  how  applying  deep  learning  methods  to  these  problems  can  produce  betteroutcomes than standard methods in finance or in Machine Learning

This work has been supervised by Professor Ali Hirsa and Teacher Assistant Francois Fagan during the Spring of 2018 at Columbia SEAS (IEORE4720).

In this repository, we only present the code related to our work with the IBB index. To obtain the same results with another index (such as the S&P500 as presented in our paper), one would simply use the appropriate list of stocks data (can be easily find using the Yahoo finance API and the code IBB-Data-Extraction.ipynb by modifying "IBB" in the code by the name of the index one wants to replicate).

## What is included in this repos ?
We included in our github repository the following files:
1. **IBB_holdings.csv**: a csv file containing the list of tickers for the IBB index
2. **IBB-Data-Extraction.ipynb**: a jupyter notebook to automatically gather the data using Yahoo Finance API
3. **IBB-Replication.ipynb**: a jupyter notebook explaining step by step the Deep Learning method we used to replicate the IBB
4. **Deep Learning for Finance - Deep Portfolio.pdf**: a paper presenting the results obtained during the semester

