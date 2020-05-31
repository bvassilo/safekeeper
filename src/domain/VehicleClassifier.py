
import IncidentClassifier

class VehicleClassifier(IncidentClassifier.IncidentClassifier):
    def __init__(self, incidentOccured, isVehicle):
        super().__init__(self, incidentOccured)
        self.isVehicle = isVehicle