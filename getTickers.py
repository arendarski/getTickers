def getTickers(index = '^dji', data_source ='stooq'):
# data_download_source = 'yahoo' # select : 'yahoo' or stooq'
    import pandas as pd

#     """ This function downloads a list of tickers of selected index from stooq.com """"

#     Parameters
#     ----------
#     index : string
#        List of potential indices ['^dji', '^spx', '^ndq', '^DAX', 'WIG20', ]  
#        Please check if selected index has this type of page as DAX : https://stooq.com/q/i/?s=^dax
#     data_source : string
#         Select: ['yahoo','stooq']
#         Select the source of historical data to return tickers appropriately, i.e. BAC or BAC.US

#     Returns
#     -------
#     tickers : list
#         The list of tickers                   
                                       
    tickers = []
    url = f'https://stooq.pl/q/i/?s={index}&i'
    print(f'Getting tickers from page number: 1')
    data = pd.read_html(url) 
    # clean_table(data)
    data = data[0].iloc[1:]
    new_header = data.iloc[0] #grab the first row for the header
    data = data[3:] #take the data less the header row
    data.columns = new_header #set the header row as the df header

    # iterate through the column with tickers at the first page
    for ticker in data.iloc[:,0]:
        if data_source == 'yahoo':
            if str('nan') not in str(ticker):
                tickers.append(ticker.split('.')[0])
        else:
            if str('nan') not in str(ticker):
                tickers.append(ticker)      
    print(f'Tickers collected so far: {len(tickers)}')
    print('---')
    # iterate through the column with tickers for the next pages, break the loop when the last page with tickers is found 
    for page in range(2, 100, 1):        
        url = f'https://stooq.pl/q/i/?s={index}&l={page}&i'
        print(f'Getting tickers from page number: {page}')
        data = pd.read_html(url)
        data = data[0].iloc[1:]
        new_header = data.iloc[0] 
        data = data[3:] 
        data.columns = new_header
        for ticker in data.iloc[:,0]:
            if data_source == 'yahoo':
                tickers_len = len(tickers)
                if str('nan') not in str(ticker):
                    tickers.append(ticker.split('.')[0])
            else:
                if str('nan') not in str(ticker):
                    tickers.append(ticker)
        print(f'Tickers collected so far: {len(tickers)}')
        print('---')
        if len(data.iloc[:,0]) == 2:
            break
    print(f'Total tickers collected: {len(tickers)}')    
    return tickers    

# Example

print(getTickers(index = '^spx', data_source ='yahoo'))
