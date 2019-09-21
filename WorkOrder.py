class WorkOrder:
	def __init__(self,workID,facility,equipment,equipmentID,priority,time,submissionTime,inProgress):
		self.workID = workID
		self.facility = facility
		self.equipment = equipment
		self.equipmentID = equipmentID
		self.priority = priority
		self.time = time
		self.submissionTime = submissionTime
		self.inProgress = inProgress;

	def getWorkID(self):
		return self.workID

	def getFacility(self):
		return self.facility

	def getEquipment(self):
		return self.equipment

	def getEquipmentID(self):
		return self.equipmentID

	def getPriority(self):
		return self.priority

	def getTime(self):
		return self.time
	
	def getSubmissionTime(self):
		return self.submissionTime

	def getStatus(self):
		return self.inProgress