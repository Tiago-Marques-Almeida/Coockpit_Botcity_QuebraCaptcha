import time
import os
import configCoockpit
import pyautogui

from datetime import datetime, timedelta
from botcity.core import DesktopBot

class Bot(DesktopBot):
    def __init__(self):
        super().__init__()
        self.dia_anterior = datetime.now() - timedelta (1)
        self.data_pasta = self.dia_anterior.strftime('%d-%m-%Y')
        self.cria_diretorio()
        
    def cria_diretorio(self):
        caminho = configCoockpit.DIRETORIO_ARQUIVOS + '\\' + self.data_pasta
        if not os.path.isdir(caminho):
            os.mkdir(caminho)

    def aguarda_download(self):
        seconds = 1
        caminhoDownload = configCoockpit.DIRETORIO_ARQUIVOS + '\\' + self.data_pasta
        time.sleep(seconds)
        dl_wait = True
        while dl_wait and seconds < 60:
            time.sleep(2)
            dl_wait = False
            for fname in os.listdir(caminhoDownload):
                if fname.endswith('.crdownload'):
                    dl_wait = True
            seconds += 1
        return seconds

    def renomar_arquivo(self, original, alterar):
        #self.convert_to_parquet(original)
        self.aguarda_download()
        os.rename(original, alterar)


    def prepara_ambiente(self):
        print('Preparando ambiente para evitar erros...')

        #Minimiza todos os programas e move o mause para o canto da tela
        pyautogui.keyDown('win')
        pyautogui.press('d')
        pyautogui.keyUp('win')
        pyautogui.moveTo(1,1)
    

    def loguin(self):
        print('Realizando Loguin...')

        #self.execute(r'C:\Users\Public\Desktop\Google Chrome')
        self.browse('https://www.cockpit.com.br/inventory/list-vehicle')
        self.maximize_window()

        #insere e-mail
        try:
            if not self.find( "e-mail", matching=0.97, waiting_time=10000):
                self.not_found("e-mail")
            self.click()
            
            self.paste('tecnologia@b.car')
        except ValueError:
            if not self.find( "edge_min", matching=0.97, waiting_time=10000):
                self.not_found("edge_min")
            self.click_relative(24, 17)

            self.maximize_window()

            if not self.find( "e-mail", matching=0.97, waiting_time=10000):
                self.not_found("e-mail")
            self.click()
            self.paste('tecnologia@b.car')

        #clica fora da caixa de e-mail
        if not self.find( "ja", matching=0.97, waiting_time=50000):
            self.not_found("ja")
        self.double_click()        
        
        #insere senha
        if not self.find( "senha", matching=0.97, waiting_time=50000):
            self.not_found("senha")
        self.click()
        
        self.paste('bcar-POCO-44')

        #clica fora da caixa de senha
        if not self.find( "ja", matching=0.97, waiting_time=50000):
            self.not_found("ja")
        self.double_click()
        
        #clica em continuar
        if not self.find( "acessar_coockpit", matching=0.97, waiting_time=50000):
            self.not_found("acessar_coockpit")
        if not self.find( "acessar_coockpit", matching=0.97, waiting_time=50000):
            print('procurando')
        self.click()


    def abre_pagina_extracao(self):
        print('Abrindo página de extração...')
        
        #aguarda a página carregar
        if not self.find( "aguarda", matching=0.97, waiting_time=10000):
            self.not_found("aguarda")               
        
        #acessar pagina de extração
        self.browse('https://www.cockpit.com.br/inventory/php/gestao-estoque/consultar')
        

    def fechar_modal(self):
        print('Fechando modal, caso haja...')
        try:
            #clica para fechar modal
            if not self.find( "continuar", matching=0.97, waiting_time=50000):
                self.not_found("continuar")
            self.click_relative(15, 12)
        except ValueError:
            print('Modal não apareceu.')


    def exporta_relatorio(self):
        print('Exportando relatório...')
        
        #rola até início da página
        self.scroll_up(9999)
        time.sleep(2)

        #clica em exportar
        if not self.find( "exportar", matching=0.97, waiting_time=50000):
            self.not_found("exportar")
        self.click()
        
        #clica em exportar csv
        if not self.find( "exportar_csv", matching=0.97, waiting_time=10000):
            self.not_found("exportar_csv")
        self.click_relative(48, 11)
        
        
    def renomeia_arquivo_e_move(self):
        print('Renomeando e salvando arquivo...')
        #clica em salvar como
        if not self.find( "salvar_como", matching=0.97, waiting_time=10000):
            self.not_found("salvar_como")
        self.click()
        
        #clica para preencher o nome
        try:
            if not self.find( "click_for_save", matching=0.97, waiting_time=10000):
                self.not_found("click_for_save")
            self.click_relative(7, 40)
        except ValueError:    
            if not self.find( "click_nome", matching=0.97, waiting_time=10000):
                self.not_found("click_nome")
            self.click_relative(6, 41)
            
        
        self.control_a()
        self.delete()
        caminho_fim = configCoockpit.DIRETORIO_ARQUIVOS + '\\' + self.data_pasta + '\\' + 'arquivo_coockpit.csv' 
        self.paste(caminho_fim)

        #clica em salvar
        if not self.find( "salvar", matching=0.97, waiting_time=10000):
            self.not_found("salvar")
        self.click()
        

        #aguarda download
        self.aguarda_download()
        
        


    def logout(self):
        print('Fazendo Logout...')
        #faz logout
        self.browse('https://www.cockpit.com.br/logout')

        #aguarda página fazer logout
        if not self.find( "ja", matching=0.97, waiting_time=90000):
            print('fechei sem aguardar')

        #fecha navegador
        self.alt_f4()


        



    def action(self, execution=None):
        self.prepara_ambiente()
        self.loguin()
        self.abre_pagina_extracao()
        self.fechar_modal()
        self.exporta_relatorio()
        self.renomeia_arquivo_e_move()
        self.logout()

            
        
        

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    tentativas = 0
    while (tentativas<10):
        try:
            Bot.main()
            tentativas = 10
        except Exception as e:
            print(e)
            tentativas += 1
            if (tentativas >=10):
                with open (r'C:\BotCoockpit\BotCoockpit\log\log.txt', 'w') as arq:
                    arq.write(str(e))
            
        os.system("taskkill /F /IM msedge.exe")
        time.sleep(30)
























