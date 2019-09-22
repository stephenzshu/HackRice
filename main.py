import pandas as pd
import queue
from queue import PriorityQueue
import WorkOrder
from WorkOrder import WorkOrder
import Worker
from Worker import Worker
import Facility
from Facility import Facility
import sys

workers = []
facility1 = Facility('Fac1',0,0,PriorityQueue(),PriorityQueue())
facility2 = Facility('Fac2',0,0,PriorityQueue(),PriorityQueue())
facility3 = Facility('Fac3',0,0,PriorityQueue(),PriorityQueue())
facility4 = Facility('Fac4',0,0,PriorityQueue(),PriorityQueue())
facility5 = Facility('Fac5',0,0,PriorityQueue(),PriorityQueue())

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
		worker = Worker(data[0],data[1],data[2],0,0)
		workers.append(worker)
	

def updateWorkQueues():
	df = pd.read_excel(r'router/RiceHackathonFile.xlsx', sheet_name='Work Order Examples')
	#print (df)
	
	for index, data in df.iterrows():
		#print(index, row)
		work = WorkOrder(data[0],data[1],data[2],data[3],data[4],data[5],data[6],False)
		if data[1] == 'Fac1':
			facility1.readyQ.put((work.priority,work))
		elif data[1] == 'Fac2':
			facility2.readyQ.put((work.priority,work))
		elif data[1] == 'Fac3':
			facility3.readyQ.put((work.priority,work))
		elif data[1] == 'Fac4':
			facility4.readyQ.put((work.priority,work))
		else:
			facility5.readyQ.put((work.priority,work))

def retrieveWork(workerName): #takes in a string from server, and returns a work order for them
	for worker in workers:
		if worker.name == workerName:
			print(worker.current_task)
			sys.stdout.flush()

def getWorkAtFacility(worker):  #is returned a work. The work is already set to the activeQ in the facility class.
	print ("GET WORK AT FACILITY ****************************************")
	work = 0
	if worker.current_facility == 'Fac1':
		work = facility1.getWork(worker)
	elif worker.current_facility == 'Fac2':
		work = facility2.getWork(worker)
	elif worker.current_facility == 'Fac3':
		work = facility3.getWork(worker)
	elif worker.current_facility == 'Fac4':
		work = facility4.getWork(worker)
	else: 
		work = facility5.getWork(worker)
	if work == 0:
		worker.current_facility = 0
		getWork(worker)
	worker.current_facility = work.facility
	worker.current_task = work.workID

def getWork(worker):
	if worker.current_facility == 0:
		work1 = facility1.peekWork(worker)
		print("Peeked Work 1")
		work2 = facility2.peekWork(worker)
		print("Peeked Work 2")
		work3 = facility3.peekWork(worker)
		print("Peeked Work 3")
		work4 = facility4.peekWork(worker)
		print("Peeked Work 4")
		work5 = facility5.peekWork(worker)
		print("Peeked Work 5")
		pq = PriorityQueue()
		if work1 is not None:
			pq.put(work1)
		if work2 is not None:
			pq.put(work2)
		if work3 is not None:
			pq.put(work3)
		if work4 is not None:
			pq.put(work4)
		if work5 is not None:
			pq.put(work5)
		work = pq.get()
		if work is not None:
			print(work)
			print("work is not none")
			print(work[1].facility)
		if work is None:
			print("FATAL ERROR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
		if work[1].facility == 'Fac1':
			work = facility1.getWork(worker)
		elif work[1].facility == 'Fac2':
			work = facility2.getWork(worker)
		elif work[1].facility == 'Fac3':
			work = facility3.getWork(worker)
		elif work[1].facility == 'Fac4':
			work = facility4.getWork(worker)
		else: 
			work = facility5.getWork(worker)
		if work is None:
			print(work)
		worker.current_facility = work[1].facility
		worker.current_task = work[1].workID
	else:
		getWorkAtFacility(worker)

def checkQueues():
	#while not facility1.readyQ.empty():
	#	print(facility1.readyQ.get()[1].workID)
	#while not facility2.readyQ.empty():
	#	print(facility2.readyQ.get()[1].workID)
	#while not facility3.readyQ.empty():
	#	print(facility3.readyQ.get()[1].workID)
	print("CHECK QUEUE")
	temp = PriorityQueue()
	count = 0
	while not facility4.readyQ.empty():
		temp.put(facility4.readyQ.get())
		count+=1
		print(count)
	while not temp.empty():
		facility4.readyQ.put(temp.get())	
	#while not facility5.readyQ.empty():
	#	print(facility5.readyQ.get()[1].workID)

def main():
	updateFacility()
	print('Updated Facilities \n')
	updateWorkers()
	print('Updated Workers \n')
	updateWorkQueues()
	print('Updated Work Queues \n')
	#checkQueues()
	for worker in workers:
		if worker.current_facility == 0:
			worker.current_task = getWork(worker)
			print(worker.name)
	print("DONE")
	if sys.argv[1] == 'retrieveWork':
		retrieveWork(sys.argv[2])

if __name__== "__main__":
	main()


#print (w1.__dict__.keys())
#print (w1.__dict__.values())