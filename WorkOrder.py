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

	def __lt__(self, other):
		return self.workID < other.workID
	def __gt__(self, other):
		return self.workID > other.workID
	def __eq__(self, other):
		return self.workID == other.workID
	def __le__(self, other):
		return self.workID <= other.workID
	def __ge__(self, other):
		return self.workID >= other.workID
	def __ne__(self, other):
		return self.workID != other.workID

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

	def __str__(self):
		return self.workID + " " + self.facility + " " + self.equipment + " " + self.equipmentID + " " + self.priority + " " + self.time + " " + self.submissionTime + " " + self.inProgress