import sys  
from PyQt5.QtWidgets import   QApplication,  QWidget
      
if __name__ == '__main__':
            app = QApplication(sys.argv)
            q = QWidget()
            q.show()
            sys.exit(app.exec_())
