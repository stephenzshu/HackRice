import pandas as pd
import queue
from queue import PriorityQueue
import WorkOrder
from WorkOrder import WorkOrder
import Worker
from Worker import Worker

def updateWorkers():
	df = pd.read_excel(r'router/RiceHackathonFile.xlsx', sheet_name='Worker Details')
	workers = []
	for index, data in df.iterrows():
		worker = Worker(data[0],data[1],data[2])
		workers.append(worker)
	

def updateWorkQueues():
	df = pd.read_excel(r'router/RiceHackathonFile.xlsx', sheet_name='Work Order Examples')
	#print (df)
	facility1 = PriorityQueue()
	facility2 = PriorityQueue()
	facility3 = PriorityQueue()
	facility4 = PriorityQueue()
	facility5 = PriorityQueue()
	for index, data in df.iterrows():
		#print(index, row)
		work = WorkOrder(data[0],data[1],data[2],data[3],data[4],data[5],data[6],False)
		if data[1] == 'Fac1':
			facility1.put(work.getPriority(),work)
		elif data[1] == 'Fac2':
			facility2.put(work.getPriority(),work)
		elif data[1] == 'Fac3':
			facility3.put(work.getPriority(),work)
		elif data[1] == 'Fac4':
			facility4.put(work.getPriority(),work)
		else:
			facility5.put(work.getPriority(),work)
		index+=1

def main():
	updateWorkers()
	updateWorkQueues()
  
if __name__== "__main__":
	main()

#print (w1.__dict__.keys())
#print (w1.__dict__.values())