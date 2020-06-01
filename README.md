This function downloads a list of tickers of selected index from stooq.com
Pandas library is recquired - > [https://pandas.pydata.org/]

Parameters
----------
- index : string, 
  - List of potential indices ['^dji', '^spx', '^ndq', '^DAX', 'WIG20', ], 
  - Please check if selected index has this type of page as DAX : https://stooq.com/q/i/?s=^dax
- data_source : string
  - Select: ['yahoo','stooq']
  - Select the source of historical data to return tickers appropriately, i.e. BAC or BAC.US

Returns
-------
- tickers : list
  - The list of tickers  
  
Examples
-------
- getTickers(index = '^spx', data_source ='yahoo')
- getTickers(index = '^DAX', data_source ='yahoo')
- getTickers(index = '^ndq', data_source ='stooq')
