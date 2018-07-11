class LogicGate:
    def __init__(self, n):
        self.name = n
        self.output = None

    def get_name(self):
        return self.name

    def get_output(self):
        return self.perform_gate_logic()


class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        if self.pinA is None:
            return int(input("enter pinA:" + self.get_name()))
        else:
            return self.pinA.getFrom().get_output()

    def get_pinB(self):
        if self.pinB is None:
            return int(input("enter pinB:" + self.get_name()))
        else:
            return self.pinB.getFrom().getFrom().get_output()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    def perform_gate_logic(self):

        a = self.get_pinA()
        b = self.get_pinB()

        if a == 1 & b == 1:
            return 1
        else:
            return 0

class Connector:
    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fgate

    def getTo(self):
        return self.tgate

def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    c = Connector(g1, g2)
    print(g2.get_output())

main()


