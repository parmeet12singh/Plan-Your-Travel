import re

def read_tables(soup):

    tables = soup.find_all("table",{"class":"wikitable sortable"})

    for table in tables:

        temp_airlinesWithDestinations = read_rows(table)      
        
        if(temp_airlinesWithDestinations):
            return temp_airlinesWithDestinations

def read_rows(table):
    
    rows = table.find_all('tr')

    temp_airlinesWithDestinations = []
    
    for row in rows:

        cols_headers = row.find_all('th')
        for cols_header in cols_headers:
            if(cols_header.text != 'Airlines'):
                return
            else:
                break

        result = read_cols(row)

        if result is not None:
            if(not(result[0]=='' and result[1]=='')):
                temp_airlinesWithDestinations.append(result)

    return temp_airlinesWithDestinations
    
def read_cols(row):

    cols = row.find_all('td')
    
    count_col = 0

    airline = ''
    cities = ''

    for col in cols:
                
        count_col = count_col + 1
        # Columne 1 = Airline
        if(count_col==1):
            # Removing paranthesis and its contents
            airline = re.sub("[\(\[].*?[\)\]]", '', col.text.strip().replace('\n',''))
            # Ignoring tables other than airlines-and-destinations by checking column 1 of the particular table
            if not re.match('[a-zA-Z\s]+$', airline):
                return
        # Columne 2 = Cities
        elif(count_col==2):
            # Removing paranthesis and its contents and deleting empty strings from list
            # cities = list(filter(None, re.sub("[\(\[].*?[\)\]]", '', col.text.strip().replace('\n','').replace(' ','').replace('Seasonal:',',').strip(',')).split(',')))
            cities = list(filter(None, re.sub("[\(\[].*?[\)\]]", '', col.text.strip().replace('\n','').replace('Seasonal:',',').strip(',')).split(',')))
            cities = list(map(lambda city: city.strip(' '), cities))
        else:
            break
    
    return([airline,cities])