import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd


def calplot():
    def calcurve(noise):
        return 1/np.log(np.arange(0.1,100) + noise*np.random.rand(100))
    fig = plt.figure()
    nrs = [calcurve(20),calcurve(30), calcurve(21)]
    plt.plot(np.array(nrs).transpose())
    plt.ylim([0,1])
    plt.xlabel('time')
    plt.ylabel('error')
    plt.title('calibration')
    return fig


class AlcoholTester():
    def calibrate():
        params = {'temperature' : 10,
                'humidity' : 20,
                'instrument_name' : 'alci_top_100',
                'driver_version' : 'v0.4',
                'frequency' : '200',
                'rate': '3000',
                'flow' : '231',
                'mass_constant' : '30',
                'serial_nr' : 'KTK-324-MHT-332',
                'method' :  'auto',
                'display' : 'false',
                'resolution' : '20'}
        return params, calplot()

    def measure(parameters):
        testers = ['alcohol']
        wine_path = './winequality-red.csv'
        data = pd.read_csv(wine_path, sep=';')
        data = data[testers]
        plt.style.use('seaborn-notebook')
        fig = plt.figure()
        fig.set_figwidth(6)
        fig.set_figheight(5)
        plt.plot(data[testers[0]], 'o')
        plt.xlabel('wine nr.')
        plt.ylabel(testers[0])
        return data.to_csv(sep=';'), fig

class AcidTester():

    def calibrate():
        params = {'temperature' : 10,
                'humidity' : 20,
                'instrument_name' : 'sweet_and_sour-334',
                'driver_version' : 'v1.2',
                'frequency' : '230',
                'rate': '3000',
                'flow' : '231',
                'mass_constant' : '30',
                'serial_nr' : 'Mkwe-223-320',
                'method' :  'auto',
                'display' : 'false',
                'resolution' : '20'}
        return params, calplot()
    def measure(parameters):
        testers = ['fixed acidity', 'volatile acidity', 'citric acid', 'pH']
        wine_path = './winequality-red.csv'
        data = pd.read_csv(wine_path, sep=';')
        data = data[testers]
        plt.style.use('seaborn-notebook')
        fig, axs = plt.subplots(nrows=len(testers),ncols=1)
        fig.set_figwidth(6)
        fig.set_figheight(5 * len(testers))
        for idx, col in enumerate(data[testers]):
            axs.flatten()[idx].plot(data[col], 'o')
            axs.flatten()[idx].set_xlabel('wine nr.')
            axs.flatten()[idx].set_ylabel(testers[idx])
        return data.to_csv(sep=';'), fig

class SulfurTester():
    def calibrate():
        params = {'temperature' : 10,
                'humidity' : 20,
                'instrument_name' : 'sulfi-20',
                'driver_version' : 'v2.3_fk',
                'frequency' : '230',
                'rate': '3000',
                'flow' : '231',
                'mass_constant' : '30',
                'serial_nr' : 'rike-dkeo-meow',
                'method' :  'auto',
                'display' : 'false',
                'resolution' : '20',
                'temperature_offset' : '0'}
        return params, calplot()
    def measure(parameters):
        testers = ['free sulfur dioxide', 'total sulfur dioxide', 'sulphates']
        wine_path = './winequality-red.csv'
        data = pd.read_csv(wine_path, sep=';')
        data = data[testers]
        if parameters['temperature_offset'] != 'auto':
            mod = np.array(data[testers])
            randomized = np.random.rand(mod.shape[0],mod.shape[1])
            for idx, col in enumerate(randomized.transpose()):
                data[testers[idx]] = col
        plt.style.use('seaborn-notebook')
        fig, axs = plt.subplots(nrows=len(testers),ncols=1)
        fig.set_figwidth(6)
        fig.set_figheight(5 * len(testers))
        for idx, col in enumerate(data[testers]):
            axs.flatten()[idx].plot(data[col], 'o')
            axs.flatten()[idx].set_xlabel('wine nr.')
            axs.flatten()[idx].set_ylabel(testers[idx])
        return data.to_csv(sep=';'), fig

class SugarTester():
    def calibrate():
        params = {'temperature' : 10,
                'humidity' : 20,
                'instrument_name' : 'KK-20',
                'driver_version' : 'v0.1',
                'frequency' : '230',
                'rate': '3000',
                'flow' : '231',
                'mass_constant' : '30',
                'serial_nr' : 'WSO_34_15',
                'method' :  'auto',
                'display' : 'false',
                'resolution' : '20',
               'inlet_pressure' : '1040',
               'outlet_pressure' : '330'}
        return params, calplot()
    def measure(parameters):
        testers = ['residual sugar', 'chlorides', 'density']
        wine_path = './winequality-red.csv'
        data = pd.read_csv(wine_path, sep=';')
        data = data[testers]
        plt.style.use('seaborn-notebook')
        fig, axs = plt.subplots(nrows=len(testers),ncols=1)
        fig.set_figwidth(6)
        fig.set_figheight(5 * len(testers))
        for idx, col in enumerate(data[testers]):
            axs.flatten()[idx].plot(data[col], 'o')
            axs.flatten()[idx].set_xlabel('wine nr.')
            axs.flatten()[idx].set_ylabel(testers[idx])

        return data.to_csv(sep=';'), fig


class CellarIoT():
    def measure():
        temp = round(11 + random.random()/20, 2)
        hum = round(20 + random.random()/10, 2)
        return {'cellar_temperature' : temp, 'cellar_humidity': hum }