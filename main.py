from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
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

    @Slot(str)
    def connect_to_port(self, port_name):
        print(f"Connecting to {port_name}")
        self.serial.setPortName(port_name)
        if not self.serial.open(QSerialPort.OpenModeFlag.ReadWrite):
            print(self.serial.error())

    @Slot()
    def rescan(self):
        for port in QSerialPortInfo.availablePorts():
            if "usb" in port.description().lower():
                self.cb_ports.addItem(port.portName())

    @Slot()
    def send_data(self):
        data = self.tb_send_data.text() + '\n'
        if self.serial.write(data.encode()) != -1:
            print(f"Sent data: {data}")

    @Slot()
    def read_data(self):
        self.received_data += self.serial.readAll().data().decode()
        if self.received_data[-1] == '\n':
            self.tb_received_data.insertPlainText(f"Received data: {self.received_data}")
            self.received_data = ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
