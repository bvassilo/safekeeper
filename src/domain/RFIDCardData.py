from hardware import RFIDCardScanner

class RFIDCardData:
    def __init__(self, expiration, employeeId, isGuest):
        self.expiration = expiration
        self.employeeId = employeeId
        self.isGuest = isGuest

    def writeRFIDCard(self):
        print('write rfid card')
    
    @staticmethod
    def readRFIDCardData():
        return None, False # return data, succes

    @staticmethod
    def isRFIDCardExpired(card):
        return False # todo: implement
    
    