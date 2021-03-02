#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:16:52 2020

@author: kelly
"""
from simple_port import *
import datetime as dt 
import pandas as pd 

if __name__=='__main__': 
    
    tickers = ['GOOGL', 'NEE','AMD','KO']
    start = dt.datetime(2019,1,1)
    end = dt.datetime(2019,12,31)
    port = portfolio(4, 10000,tickers,start,end, 0)
    df,max_sharpe_port = port.Find_Sharpe_Ratio()
    pd.set_option('max_columns', None)
    print(df)
    print("Num of NaN in port_risk:",df['port_risk'].isnull().sum(axis = 0))
    print("average return of all portfolio: ", df['expected_return'].mean())
    print("SP500 return:", port.sp500)
    print("the portfolio with maximal sharpe ratio:\n", max_sharpe_port)    
    
    
'''Result
  
sharpe  expected_return  port_risk        w1        w2        w3  \       
0     0.002236         0.001428   0.638333  0.312500  0.375000  0.125000   
1     0.001625         0.001174   0.722395  0.555556  0.444444  0.000000   
2     0.002156         0.001377   0.638596  0.333333  0.291667  0.125000   
3     0.002579         0.001610   0.624396  0.275862  0.310345  0.206897   
4     0.001556         0.001199   0.770646  0.666667  0.083333  0.083333   
5     0.001646         0.001222   0.742329  0.285714  0.000000  0.142857   
6     0.001680         0.001189   0.707947  0.133333  0.333333  0.066667   
7     0.003302         0.002129   0.644861  0.157895  0.210526  0.421053   
8     0.003546         0.002368   0.667820  0.000000  0.285714  0.500000   
9     0.001598         0.001162   0.727505  0.583333  0.416667  0.000000   
10    0.002370         0.001500   0.633090  0.240000  0.360000  0.160000   
11    0.003456         0.002317   0.670573  0.062500  0.187500  0.500000   
12    0.002706         0.001709   0.631580  0.142857  0.321429  0.250000   
13    0.002931         0.001926   0.656945  0.363636  0.272727  0.318182   
14    0.002821         0.001859   0.659054  0.192308  0.115385  0.346154   
15    0.001848         0.001321   0.715080  0.562500  0.125000  0.125000   
16    0.002675         0.001773   0.662649  0.050000  0.450000  0.250000   
17    0.002101         0.001532   0.729046  0.470588  0.000000  0.235294   
18    0.003349         0.002216   0.661832  0.000000  0.416667  0.416667   
19    0.003206         0.002052   0.640068  0.238095  0.238095  0.380952   
20    0.002392         0.001535   0.641636  0.350000  0.200000  0.200000   
21    0.002265         0.001608   0.710067  0.090909  0.090909  0.272727   
22    0.001864         0.001330   0.713876  0.058824  0.352941  0.117647   
23    0.001726         0.001171   0.678713  0.227273  0.363636  0.045455   
24    0.001590         0.001107   0.696003  0.529412  0.352941  0.000000   
25    0.003085         0.002336   0.757309  0.000000  0.000000  0.555556   
26    0.003448         0.002222   0.644429  0.105263  0.368421  0.421053   
27    0.001645         0.001240   0.753974  0.230769  0.000000  0.153846   
28    0.001336         0.001013   0.758310  0.375000  0.000000  0.062500   
29    0.002265         0.001608   0.710067  0.090909  0.090909  0.272727   
       ...              ...        ...       ...       ...       ...   
9970  0.001831         0.001329   0.725627  0.444444  0.000000  0.166667   
9971  0.002429         0.001623   0.668049  0.304348  0.086957  0.260870   
9972  0.002392         0.001531   0.640054  0.333333  0.200000  0.200000   
9973  0.003382         0.002163   0.639501  0.176471  0.294118  0.411765   
9974  0.003625         0.002533   0.698854  0.181818  0.272727  0.545455   
9975  0.002276         0.001508   0.662467  0.111111  0.388889  0.166667   
9976  0.003430         0.002309   0.673068  0.083333  0.166667  0.500000   
9977  0.002786         0.001813   0.650550  0.272727  0.136364  0.318182   
9978  0.002449         0.001641   0.669969  0.227273  0.090909  0.272727   
9979  0.002315         0.001484   0.641099  0.318182  0.409091  0.136364   
9980  0.002491         0.001606   0.644798  0.280000  0.160000  0.240000   
9981  0.003138         0.001962   0.625316  0.166667  0.333333  0.333333   
9982  0.001676         0.001296   0.773118  0.000000  0.214286  0.142857   
9983  0.002903         0.001826   0.628970  0.192308  0.230769  0.307692   
9984  0.003229         0.002094   0.648338  0.052632  0.421053  0.368421   
9985  0.003823         0.002884   0.754362  0.000000  0.200000  0.700000   
9986  0.001844         0.001220   0.661328  0.291667  0.250000  0.083333   
9987  0.002226         0.001495   0.671764  0.086957  0.347826  0.173913   
9988  0.003683         0.002890   0.784506  0.000000  0.090909  0.727273   
9989  0.001877         0.001232   0.656274  0.285714  0.321429  0.071429   
9990  0.001571         0.001125   0.716459  0.200000  0.500000  0.000000   
9991  0.002988         0.001905   0.637738  0.307692  0.307692  0.307692   
9992  0.001050         0.000910   0.866854  0.000000  0.250000  0.000000   
9993  0.002649         0.001655   0.624744  0.290323  0.290323  0.225806   
9994  0.001510         0.001026   0.679496  0.380952  0.285714  0.000000   
9995  0.002644         0.001724   0.652001  0.400000  0.250000  0.250000   
9996  0.003895         0.002982   0.765685  0.000000  0.285714  0.714286   
9997  0.002552         0.001624   0.636422  0.333333  0.380952  0.190476   
9998  0.001925         0.001265   0.657200  0.250000  0.333333  0.083333   
9999  0.003176         0.002372   0.746765  0.062500  0.000000  0.562500   


 w4  
0     0.187500  
1     0.000000  
2     0.250000  
3     0.206897  
4     0.166667  
5     0.571429  
6     0.466667  
7     0.210526  
8     0.214286  
9     0.000000  
10    0.240000  
11    0.250000  
12    0.285714  
13    0.045455  
14    0.346154  
15    0.187500  
16    0.250000  
17    0.294118  
18    0.166667  
19    0.142857  
20    0.250000  
21    0.545455  
22    0.470588  
23    0.363636  
24    0.117647  
25    0.444444  
26    0.105263  
27    0.615385  
28    0.562500  
29    0.545455  
       ...  
9970  0.388889  
9971  0.347826  
9972  0.266667  
9973  0.117647  
9974  0.000000  
9975  0.333333  
9976  0.250000  
9977  0.272727  
9978  0.409091  
9979  0.136364  
9980  0.320000  
9981  0.166667  
9982  0.642857  
9983  0.269231  
9984  0.157895  
9985  0.100000  
9986  0.375000  
9987  0.391304  
9988  0.181818  
9989  0.321429  
9990  0.300000  
9991  0.076923  
9992  0.750000  
9993  0.193548  
9994  0.333333  
9995  0.100000  
9996  0.000000  
9997  0.095238  
9998  0.333333  
9999  0.375000  



[10000 rows x 7 columns]
Num of NaN in port_risk: 0
average return of all portfolio:  0.0016945710134058532
SP500 return: 0.0010067324577177116

the portfolio with maximal sharpe ratio:
sharpe             0.003894
expected_return    0.003011
port_risk          0.773167
w1                 0.000000
w2                 0.272727
w3                 0.727273
w4                 0.000000
'''