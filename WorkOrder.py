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

	#flipped for everything because less priority and less time is better
	def __lt__(self, other):
		return ((self.priority,self.time) < (other.priority, other.time))
	def __gt__(self, other):
		return ((self.priority,self.time) > (other.priority, other.time))
	def __eq__(self, other):
		return ((self.priority,self.time) == (other.priority, other.time))
	def __le__(self, other):
		return ((self.priority,self.time) <= (other.priority, other.time))
	def __ge__(self, other):
		return ((self.priority,self.time) >= (other.priority, other.time))
	def __ne__(self, other):
		return ((self.priority,self.time) != (other.priority, other.time))

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
		return str(self.workID) + " " + self.facility + " " + self.equipment + " " + self.equipmentID + " " + str(self.priority) + " " + str(self.time) + " " + str(self.submissionTime) + " " + str(self.inProgress)