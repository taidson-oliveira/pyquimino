import time, sys
import xlsxwriter
import serial
import matplotlib.pyplot as plt

class Coletor(serial.Serial):
    def __init__(self):
        serial.Serial.__init__(self)

        self.listaDados = []
        self.listaTempo = []

        try:
            #set port received data
            self.receivedSF = serial.Serial('/dev/ttyUSB2', 9600)
        except serial.serialutil.SerialException:
            return '/dev/ttyUSB_X is not connected'


    def dados(self):
        tempo_ini = time.time()
        verification = True
        while verification:
            valor = (int(self.receivedSF.readline()))
            if valor != -100:
                tempo_fim = time.time()
                tempo = tempo_fim - tempo_ini
                # tempo_ini = tempo_fim
                print(valor,tempo)
                if tempo >=1:
                    self.listaDados.append(valor)
                    self.listaTempo.append(tempo)
            else:
                verification = False


    def graph(self):
        if self.listaDados or self.listaTempo:
            plt.plot(self.listaTempo[1:-1],self.listaDados[1:-1])
            plt.show()
        else:
            self.listaDados = list(input("Digite a lista de valores no eixo x: "))
            self.listaTempo = list(input("Digite a lista de valores no eixo y: "))
            plt.plot(self.listaTempo,self.listaDados)
            plt.show()
            self.listaDados = []
            self.listaTempo = []

    def spreadsheet(self,name,row=0,col=0):
        name = name+".xlsx"
        workbook = xlsxwriter.Workbook(name)
        worksheet = workbook.add_worksheet()
        worksheet.write(0,3,"TEMPO DE REFERENCIA:")
        worksheet.write(0,4,time.time())

        for item in self.listaDados:
            worksheet.write(row, col, item)
            worksheet.write(row, col+1, self.listaTempo[col])
            row+=1

        workbook.close()

    def desconectar(self):
        self.listaDados = []
        self.listaTempo = []
        self.receivedSF.close()
