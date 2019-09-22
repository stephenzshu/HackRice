import pandas as pd
import queue
from queue import PriorityQueue
import WorkOrder
from WorkOrder import WorkOrder
import Worker
from Worker import Worker

workers = []
facility1 = []
facility2 = []
facility3 = []
facility4 = []
facility5 = []

def updateFacility():
	df = pd.read_excel(r'router/RiceHackathonFile.xlsx', sheet_name='Facility Details')
	for index, data in df.iterrows():
		if data[0] == 'Fac1':
			facility1 = Facility(data[0],data[1],data[2],PriorityQueue(),PriorityQueue())
		elif data[0] == 'Fac2':
			facility2 = Facility(data[0],data[1],data[2],PriorityQueue(),PriorityQueue())
		elif data[0] == 'Fac3':
			facility3 = Facility(data[0],data[1],data[2],PriorityQueue(),PriorityQueue())
		elif data[0] == 'Fac4':
			facility4 = Facility(data[0],data[1],data[2],PriorityQueue(),PriorityQueue())
		else:
			facility5 = Facility(data[0],data[1],data[2],PriorityQueue(),PriorityQueue())
		

def updateWorkers():
	df = pd.read_excel(r'router/RiceHackathonFile.xlsx', sheet_name='Worker Details')
	for index, data in df.iterrows():
		worker = Worker(data[0],data[1],data[2],0,0,0)
		workers.append(worker)
	

def updateWorkQueues():
	df = pd.read_excel(r'router/RiceHackathonFile.xlsx', sheet_name='Work Order Examples')
	#print (df)
	
	for index, data in df.iterrows():
		#print(index, row)
		work = WorkOrder(data[0],data[1],data[2],data[3],data[4],data[5],data[6],False)
		if data[1] == 'Fac1':
			facility1.readyQ.put(work.getPriority(),work)
		elif data[1] == 'Fac2':
			facility2.readyQ.put(work.priority,work)
		elif data[1] == 'Fac3':
			facility3.readyQ.put(work.priority,work)
		elif data[1] == 'Fac4':
			facility4.readyQ.put(work.priority,work)
		else:
			facility5.readyQ.put(work.priority,work)

def getWorkAtFacility(Worker worker): 
	if worker.current_facility == '1':
		facility1.getWork(worker)
	elif if worker.current_facility == '2':
		facility2.getWork(worker)
	elif if worker.current_facility == '3':
		facility3.getWork(worker)
	elif if worker.current_facility == '4':
		facility4.getWork(worker)
	else:
		facility5.getWork(worker)

def getWork(Worker worker):
	if worker.current_facility == 0:

	else:

def main():
	updateFacility()
	updateWorkers()
	updateWorkQueues()
	for worker in workers:
		if worker.get_status == 0:
			worker.current_task = getWork(worker)
			worker.status = 1
			
  
if __name__== "__main__":
	main()

#print (w1.__dict__.keys())
#print (w1.__dict__.values())