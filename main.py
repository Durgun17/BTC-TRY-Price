import sys
from PyQt5.QtWidgets import*
from panel import*
import requests
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


#Arayüz işlemleri
#------------------------------------------------------------

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_BitcoinFiyat()
ui.setupUi(pencere)
pencere.show()



def get_coinbase_price():
    url = "https://api.coinbase.com/v2/exchange-rates?currency=BTC"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = round(float(data['data']['rates']['TRY']), 2)
        return price
    except requests.exceptions.RequestException as e:
        raise Exception("Error fetching Coinbase data:", e)

def get_binance_price():
    url = "https://api.binance.com/api/v1/ticker/price?symbol=BTCTRY"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = round(float(data['price']), 2)
        return price
    except requests.exceptions.RequestException as e:
        raise Exception("Error fetching Binance data:", e)

def get_bitci_price():
    url = "https://api.bitci.com/api/coin/btc_TRY/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = round(float(data['price']), 2)
        return price
    except requests.exceptions.RequestException as e:
        raise Exception("Error fetching Bitci data:", e)

if __name__ == "__main__":
    try:
        coinbase_price = get_coinbase_price()
        print("Coinbase BTC/TRY Price:", coinbase_price)
        ui.lblCoinBase.setStyleSheet("font: 17pt;")
        ui.lblCoinBase.setText(str(coinbase_price))
    except Exception as e:
        print(e)

    try:
        binance_price = get_binance_price()
        print("Binance BTC/TRY Price:", binance_price)
        ui.lblBinance.setStyleSheet("font: 17pt;")
        ui.lblBinance.setText(str(binance_price))
    except Exception as e:
        print(e)

    try:
        bitci_price = get_bitci_price()
        ui.lblBitci.setStyleSheet("font: 17pt;")
        ui.lblBitci.setText(str(bitci_price))
        print("Bitci BTC/TRY Price:", bitci_price)
    except Exception as e:
        print(e)




def button_guncelle(self):
     print("----- Güncel Fiyatlar -----")
     if __name__ == "__main__":
        try:
            coinbase_price = get_coinbase_price()
            print("Coinbase BTC/TRY Price:", coinbase_price)
            ui.lblCoinBase.setStyleSheet("font: 17pt;")
            ui.lblCoinBase.setText(str(coinbase_price))
        except Exception as e:
            print(e)

        try:
            binance_price = get_binance_price()
            print("Binance BTC/TRY Price:", binance_price)
            ui.lblBinance.setStyleSheet("font: 17pt;")
            ui.lblBinance.setText(str(binance_price))
        except Exception as e:
            print(e)

        try:
            bitci_price = get_bitci_price()
            ui.lblBitci.setStyleSheet("font: 17pt;")
            ui.lblBitci.setText(str(bitci_price))
            print("Bitci BTC/TRY Price:", bitci_price)
        except Exception as e:
            print(e)



def button_clicked_Binance(self):
        url = QUrl("https://www.binance.com/tr/trade/BTC_TRY?type=spot")
        QDesktopServices.openUrl(url)

def button_clicked_CoinBase(self):
        url = QUrl("https://www.coinbase.com/tr/price/bitcoin")
        QDesktopServices.openUrl(url)

def button_clicked_Bitci(self):
        url = QUrl("https://www.bitci.com.tr/exchange/advanced/BTC_TRY")
        QDesktopServices.openUrl(url)

ui.btnBinance.clicked.connect(button_clicked_Binance)   
ui.btnCoinBase.clicked.connect(button_clicked_CoinBase)        
ui.pushButton_3.clicked.connect(button_clicked_Bitci)    
ui.guncelle.clicked.connect(button_guncelle)


sys.exit(uygulama.exec_())