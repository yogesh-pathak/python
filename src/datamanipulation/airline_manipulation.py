import pandas as pd

#Read the data/flights.csv dataset into Python
df = pd.read_csv("../../data/flights.csv")

#remove the column "DAY_OF_WEEK"
del df['DAY_OF_WEEK']
print(df.columns)

#rename the column "WHEELS_OFF" to "HAS_WHEELS"
df.rename(columns={'WHEELS_OFF':'HAS_WHEELS'})
print(df.columns)

#slice the dataset row-wise into 4 equal-sized chunks
def getChunks(lst, n):
    val = []
    for i in range(n):
        val.append(lst[i::n])
    return val

chunks = getChunks(df, 4)

# concatenate back the chucks produced above into 1 dataset
concatenatedList = [chunks[0], chunks[1], chunks[2], chunks[3]]
finalDataframe = pd.concat(concatenatedList)

#get the slice of the dataset that is only relevant to the airline AA
airlineForAA = df[df.AIRLINE == 'AA']

#get the slice of the dataset where delay is <10 and destination is PBI
delay = df[(df.WEATHER_DELAY < 10)&(df.DESTINATION_AIRPORT == 'PBI')]

#fill the blanks in the AIR_SYSTEM_DELAY column with the average of the column itself

df.AIR_SYSTEM_DELAY.fillna(df.AIR_SYSTEM_DELAY.mean())

#Create a column "has_A", which contains 1 if the airline name contains the letter 'A', 0 otherwise
df['has_A'] = df.AIRLINE.map(lambda x: '1' if 'A' in x else '0')

#get a random sample of the rows in the dataframe
df.sample(200)

#normalise the column "DEPARTURE_DELAY" to the range 0-1 with MinMax normalisation
(df.DEPARTURE_DELAY - df.DEPARTURE_DELAY.min())/(df.DEPARTURE_DELAY.max() - df.DEPARTURE_DELAY.min())

#binarise the column "ORIGIN_AIRPORT"

