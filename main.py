import pandas as pd
import queue
from queue import PriorityQueue
import WorkOrder
from WorkOrder import WorkOrder
df = pd.read_excel(r'RiceHackathonFile.xlsx', sheet_name='Work Order Examples')
#print (df)
facility1 = PriorityQueue()
facility2 = PriorityQueue()
facility3 = PriorityQueue()
facility4 = PriorityQueue()
facility5 = PriorityQueue()
index = 0
while index < 29:
	data = df.loc[index,:]
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



#print (w1.__dict__.keys())
#print (w1.__dict__.values())