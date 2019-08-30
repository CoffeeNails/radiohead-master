import pandas as pd
import csv
import math

def hexToDec(hexNum):
    hex = hexNum.replace(" ", "")
    hex = hex[4:]
    i = int(hex, 16)
    #Convert into decimal value
    dec = str(i)
    return(dec)

def read_csv(filename):
    df = pd.read_csv(filename, sep=',', header=0)
    return df

#Take each row in the 'Datablock' column and convert to decimal value
def convertToDec(df):
    L = []
    total_rows = len(df['Datablock'])
    for i in range(total_rows):
        value = (df.loc[i, ['Datablock']])
	hex=hexToDec(value[0])
	L.append(hex)
    return L

def writetocsv(filename, read_data):
    read_data.to_csv(filename, sep=',', encoding='utf-8')

read_data = read_csv('../BRMSample/build/release/data/example.csv')

computed_decimal = convertToDec(read_data)
read_data['Decimal value'] = computed_decimal

writetocsv('../BRMSample/build/release/data/result.csv', read_data)
