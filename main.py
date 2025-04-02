from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from PySide6.QtGui import QTextCursor
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from main_window_ui import Ui_MainWindow

import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.serial = QSerialPort()
        self.serial.readyRead.connect(self.read_data)
        self.received_data = ""

        self.rescan()

        for baud in QSerialPort.BaudRate:
            self.cb_baud_rate.addItem(str(baud))
        self.cb_baud_rate.setCurrentText(str(self.serial.baudRate()))

    @Slot()
    def connect(self):
        port_name = self.cb_ports.currentText()
        baud_rate = self.cb_baud_rate.currentText()
        print(f"Connecting to {port_name} with baud rate {baud_rate}")
        self.serial.setPortName(port_name)
        self.serial.setBaudRate(int(baud_rate))
        if not self.serial.open(QSerialPort.OpenModeFlag.ReadWrite):
            print(self.serial.error())

    @Slot()
    def rescan(self):
        self.cb_ports.clear()
        for port in QSerialPortInfo.availablePorts():
            if "usb" in port.description().lower():
                self.cb_ports.addItem(port.portName())

    @Slot()
    def send_data(self):
        data = self.tb_send_data.text()
        if self.serial.write(f"{data}\n".encode()) != -1:
            print(f"Sent data: {data}")

    @Slot()
    def read_data(self):
        self.received_data += self.serial.readAll().data().decode()
        if self.received_data[-1] == '\n':
            self.tb_received_data.moveCursor(QTextCursor.MoveOperation.End)
            self.tb_received_data.insertPlainText(f"Received data: {self.received_data}")
            self.received_data = ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
