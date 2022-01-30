import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from covidResponse.settings import MEDIA_ROOT

def readData():
    data_loc=os.path.join(MEDIA_ROOT,'data')
    data_loc += "/dataset.csv"
    return pd.read_csv(data_loc)

def encodeData(covid):
    e=LabelEncoder()
    covid['Breathing Problem']=e.fit_transform(covid['Breathing Problem'])
    covid['Fever']=e.fit_transform(covid['Fever'])
    covid['Dry Cough']=e.fit_transform(covid['Dry Cough'])
    covid['Sore throat']=e.fit_transform(covid['Sore throat'])
    covid['Running Nose']=e.fit_transform(covid['Running Nose'])
    covid['Asthma']=e.fit_transform(covid['Asthma'])
    covid['Chronic Lung Disease']=e.fit_transform(covid['Chronic Lung Disease'])
    covid['Headache']=e.fit_transform(covid['Headache'])
    covid['Heart Disease']=e.fit_transform(covid['Heart Disease'])
    covid['Diabetes']=e.fit_transform(covid['Diabetes'])
    covid['Hyper Tension']=e.fit_transform(covid['Hyper Tension'])
    covid['Abroad travel']=e.fit_transform(covid['Abroad travel'])
    covid['Contact with COVID Patient']=e.fit_transform(covid['Contact with COVID Patient'])
    covid['Attended Large Gathering']=e.fit_transform(covid['Attended Large Gathering'])
    covid['Visited Public Exposed Places']=e.fit_transform(covid['Visited Public Exposed Places'])
    covid['Family working in Public Exposed Places']=e.fit_transform(covid['Family working in Public Exposed Places'])
    covid['Wearing Masks']=e.fit_transform(covid['Wearing Masks'])
    covid['Sanitization from Market']=e.fit_transform(covid['Sanitization from Market'])
    covid['COVID-19']=e.fit_transform(covid['COVID-19'])
    covid['Dry Cough']=e.fit_transform(covid['Dry Cough'])
    covid['Sore throat']=e.fit_transform(covid['Sore throat'])
    covid['Gastrointestinal ']=e.fit_transform(covid['Gastrointestinal '])
    covid['Fatigue ']=e.fit_transform(covid['Fatigue '])
    return covid


def removeUnwantedData(covid):
    covid=covid.drop('Running Nose',axis=1)
    covid=covid.drop('Chronic Lung Disease',axis=1)
    covid=covid.drop('Headache',axis=1)
    covid=covid.drop('Heart Disease',axis=1)
    covid=covid.drop('Diabetes',axis=1)
    covid=covid.drop('Gastrointestinal ',axis=1)
    covid=covid.drop('Wearing Masks',axis=1)
    covid=covid.drop('Sanitization from Market',axis=1)
    covid=covid.drop('Asthma',axis=1) 
    return covid


def calculateInfectionProbability(covid, data):
    x=covid.drop('COVID-19',axis=1)
    y=covid['COVID-19']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    return  model.predict_proba([data])[0][1] * 100