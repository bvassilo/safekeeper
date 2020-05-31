from datetime import datetime

class AccessLog:
    @staticmethod
    def writeFailedCheckInOut(reason):
        print(f'FailedCheckInOut {reason}')

    @staticmethod
    def writeCheckInOut(user, isCheckIn):
        print(f'WriteCheckInOut {user}, check in: {isCheckIn}')

    def writeIncidentToAccessLogs(user, card, incident, details):
        time = datetime.now()
        print(f'writeIncidentToAccessLogs: {user}, {card}, {incident}, {time}')

    def writeToAccessLogs(card, reason):
        time = datetime.now()
        print(f'writeToAccessLogs: {card}, {reason}, {time}')


    @staticmethod
    def checkAccessLog():
        # dummy
        return True

    @staticmethod
    def searchBy():
        return [1, 2, 3, 4, 5]
