
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog

from Ui_CarSim import Ui_MainWindow
from Ui_About import Ui_about_dialog


class Car(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        #Setup Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Engine Status
        self.engine_status = False

        #General Window Adjustments
        self.ui.statusbar.showMessage("Welcome!", 3000)
        self.ui.actionAbout.triggered.connect(self.about)

        #Fuel Tank Values
        self.fuel_tank_capacity = 60
        self.fuel_tank = 0

        #Fuel Gauge
        self.ui.fuel_level.setMaximum(self.fuel_tank_capacity)

        #Signals and Slots
        self.ui.start_engine.clicked.connect(self.engine_start)
        self.ui.stop_engine.clicked.connect(self.engine_stop)
        self.ui.refuel.clicked.connect(self.refuel)
        self.ui.run.clicked.connect(self.run)

    #About Dialog Window
    def about(self):

        dialog = QDialog()
        dialog.ui = Ui_about_dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def refuel(self):
        """Refuels the car."""

        self.amount = self.ui.amount.text()
        self.ui.amount.clear()

        try:
            if self.engine_status == True:
                self.ui.statusbar.showMessage("Cannot refuel while engine is running!")
                print("Cannot refuel while engine is running!")

            elif self.fuel_tank == self.fuel_tank_capacity:
                self.ui.statusbar.showMessage("Tank full!")
                print("Tank full!")

            elif self.amount == "":
                f_amount = self.fuel_tank_capacity - self.fuel_tank
                self.fuel_tank = self.fuel_tank_capacity
                self.ui.fuel_level.setValue(self.fuel_tank)

                self.ui.statusbar.showMessage("Refueled {} liters!".format(f_amount))
                print("Refueled {} liters!".format(f_amount))
            
            elif int(self.amount) < 0:
                self.ui.statusbar.showMessage("Amount cannot be negative number!")
                print("Amount cannot be negative number!")
            
            elif int(self.amount) > 60:
                self.ui.statusbar.showMessage("Tank cannot hold {} liters. Capacity is {} liters.".format(
                    self.amount, self.fuel_tank_capacity))
                print("Tank cannot hold {} liters. Capacity is {} liters.".format(
                    self.amount, self.fuel_tank_capacity))

            elif (int(self.amount) <= 60) and ((int(self.amount) + self.fuel_tank) > 60):
                self.ui.statusbar.showMessage("Tank can hold only {} more liters.".format(self.fuel_tank_capacity - self.fuel_tank))
                print("Tank can hold only {} more liters.".format(self.fuel_tank_capacity - self.fuel_tank))
            
            else:
                self.fuel_tank += int(self.amount)
                self.ui.fuel_level.setValue(self.fuel_tank)

                self.ui.statusbar.showMessage("Refueled {} liters!".format(int(self.amount)))
                print("Refueled {} liters!".format(int(self.amount)))
        
        except ValueError:
            self.ui.amount.clear()
            self.ui.statusbar.showMessage("Amount have to be INT!")
            print("Amount have to be INT!")

    def engine_start(self):
        """Starts the engine."""
        if self.engine_status == True:
            self.ui.statusbar.showMessage("Engine already started!")
            print("Engine already started!")
        
        elif self.fuel_tank == 0:
            self.ui.statusbar.showMessage("Tank empty!")
            print("Tank empty!")

        else:
            self.engine_status = True

            self.ui.statusbar.showMessage("Engine started!")
            print("Engine started!")
            
    
    def engine_stop(self):
        """Stops the engine."""
        if self.engine_status == True:
            self.engine_status = False

            self.ui.statusbar.showMessage("Engine stopped!")
            print("Engine stopped!")
            
        else:
            self.ui.statusbar.showMessage("Engine already stopped!")
            print("Engine already stopped!")
    
    def run(self):
        """Moves the car."""
        try:
            self.distance = int(self.ui.distance.text())
            self.ui.distance.clear()
            
            if (self.distance > 0) and (self.engine_status == True) and (self.fuel_tank > 0):
                req_fuel = int(self.distance) * 0.093

                if req_fuel > self.fuel_tank:
                    self.ui.statusbar.showMessage("Not enough fuel!")
                    print("Not enough fuel!")
                
                else:
                    self.fuel_tank -= req_fuel
                    self.ui.fuel_level.setValue(self.fuel_tank)

                    self.ui.statusbar.showMessage("Car successfully runned {} km!".format(self.distance))
                    print("Car successfully runned {} km and consumed {} liters!".format(self.distance, req_fuel))
                    print("Fuel left: {}".format(self.fuel_tank))

            elif self.distance < 0:
                self.ui.statusbar.showMessage("Distance can't be negative!")
                print("Distance can't be negative!")

            elif self.engine_status == False:
                self.ui.statusbar.showMessage("Engine is not started!")
                print("Engine is not started!")
        
        except ValueError:
            self.ui.distance.clear()

            self.ui.statusbar.showMessage("Distance have to be INT!")
            print("Distance have to be INT!")
            

    
    @classmethod
    def helpdir(cls):
        """Help function. Currently on WIP."""
        for i in dir(Car):
            if not str(i).startswith("_"):
                print(i)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Car()
    window.show()   #Pushes created objects
    sys.exit(app.exec_())
        
