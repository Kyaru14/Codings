import builtins

from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from frontend.gui import Ui_MainWindow
from backend.Huffman import HuffmanEncoding
from backend.Shannon import ShannonCoding
from backend.Fino import FinoCoding

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)

    huffman = HuffmanEncoding()
    shannon = ShannonCoding()
    fino = FinoCoding()


    def console_print(s):
        """将控制台输出重定向至窗口下方的文本框中"""
        ui.console_box.appendPlainText(str(s))


    builtins.print = console_print

    print("""使用帮助
    1.编码：在编码内容框中输入任意消息，点击编码按钮，即可看到编码结果、码字对应关系、编码性能。若为二进制编码，还会计算压缩率。（假设消息由ASCII字符组成，即一个字符存储8bit）
    2.解码：在编码完成后，可以在编码结果框中输入任意编码组合，然后点击解码按钮，可以在编码内容框中看到解码结果。
    3.控制台输出以及系统错误输出已重定向到此处
    4.制作者：Kyaru14 学号：111111111111 2023年6月22日""")


    def exception_hook(type, value, traceback):
        """当有异常抛出时，将异常信息显示在窗口下方的文本框中"""
        ui.console_box.appendPlainText(str(type) + " " + str(value))


    def on_encode_button_h_click():
        """霍夫曼编码-编码按钮监听事件"""
        n = int(ui.n_box.text())
        r = int(ui.r_box.text())
        huffman.set_n_r(n, r)
        msg = ui.msgbox_h.toPlainText()
        encoded = huffman(msg)
        print(f"各码字出现频率：{huffman.counter}")
        coding_result = huffman.coding_result
        result = ""
        for key in coding_result:
            result += f"{key}: {coding_result[key]}\n"
        summary = huffman.summary()
        ui.coding_result_box_h.setPlainText(result)
        ui.encoded_box_h.setPlainText(encoded)
        ui.summary_box_h.setPlainText(summary)


    def on_decode_button_h_click():
        """霍夫曼编码-解码按钮监听事件"""
        encoded = ui.encoded_box_h.toPlainText()
        decoded = huffman.decode(encoded)
        ui.msgbox_h.setPlainText(decoded)


    def on_encode_button_s_click():
        """香农编码-编码按钮监听事件"""
        msg = ui.msgbox_s.toPlainText()
        encoded = shannon(msg)
        print(f"各码字出现概率：{shannon.counter}")
        coding_result = shannon.coding_result
        result = ""
        for key, value in zip(coding_result[0], coding_result[1]):
            result += f"{key}: {value}\n"
        summary = shannon.summary()
        ui.coding_result_box_s.setPlainText(result)
        ui.encoded_box_s.setPlainText(encoded)
        ui.summary_box_s.setPlainText(summary)


    def on_decode_button_s_click():
        """香农编码-解码按钮监听事件"""
        encoded = ui.encoded_box_s.toPlainText()
        decoded = shannon.decode(encoded)
        ui.msgbox_s.setPlainText(decoded)


    def on_encode_button_f_click():
        """费诺编码-编码按钮监听事件"""
        msg = ui.msgbox_f.toPlainText()
        encoded = fino(msg)
        print(f"各码字出现概率：{fino.counter}")
        coding_result = fino.coding_result
        result = ""
        for key in coding_result:
            result += f"{key}: {coding_result[key]}\n"
        summary = fino.summary()
        ui.coding_result_box_f.setPlainText(result)
        ui.encoded_box_f.setPlainText(encoded)
        ui.summary_box_f.setPlainText(summary)


    def on_decode_button_f_click():
        """费诺编码-解码按钮监听事件"""
        encoded = ui.encoded_box_f.toPlainText()
        decoded = fino.decode(encoded)
        ui.msgbox_h.setPlainText(decoded)


    # 与对应按钮绑定
    ui.encode_button_h.clicked.connect(on_encode_button_h_click)
    ui.decode_button_h.clicked.connect(on_decode_button_h_click)
    ui.encode_button_s.clicked.connect(on_encode_button_s_click)
    ui.decode_button_s.clicked.connect(on_decode_button_s_click)
    ui.encode_button_f.clicked.connect(on_encode_button_f_click)
    ui.decode_button_f.clicked.connect(on_decode_button_f_click)

    sys.excepthook = exception_hook
    win.show()
    sys.exit(app.exec())
