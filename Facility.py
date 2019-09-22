import queue
from queue import PriorityQueue
import Worker
from Worker import Worker
import WorkOrder
from WorkOrder import WorkOrder
class Facility:
    def __init__(self, name, lat, lon, readyQ, activeQ):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.readyQ = readyQ
        self.activeQ = activeQ
        #self.equipment_list = equipment_list

    def get_name(self):
        return self.name

    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    def removeActive(self, worker):
        removed = None
        temp = PriorityQueue()
        while self.activeQ.qsize() > 0:
            work = self.activeQ.get()
            if worker.current_task != work[1]:   #might need 'is' operator or update the comparator
                temp.put(work)
            else:
                removed = work
        while temp.qsize() > 0:
            self.activeQ.put(temp.get())
        return removed[1]

    def getWork(self, worker):
        temp = PriorityQueue()
        hasWork = False
        work = None
        #print(self.name)
        #print("BEFORE")
        #print(self.activeQ.qsize())
        #print(self.readyQ.qsize())
        while not self.readyQ.empty() and not hasWork:
            work = self.readyQ.get()
            #print (work[1])
            if not work[1].equipment in worker.equipment_cert.split(", "):  #put in temp queue to cycle and look for good work
                temp.put(work)
            else: #work has been found
                #print("FOUND WORK")
                #print(work[1].equipment)
                #print(worker.equipment_cert)
                while not temp.empty(): #put all the temporarily removed work back in the readyQ
                    self.readyQ.put(temp.get())
                self.activeQ.put(work)
                hasWork = True
            if self.readyQ.empty() and hasWork is False:
                #print("IM EMPTY")
                while not temp.empty(): #put all the temporarily removed work back in the readyQ
                    self.readyQ.put(temp.get())
                break
        #print(self.readyQ.empty())
        #print(work[1])
        #print(hasWork)
        #print("AFTER")
        #print(self.activeQ.qsize())
        if hasWork is False:
            return None
        return work[1]

    def peekWork(self, worker):
        temp = PriorityQueue()
        hasWork = False
        work = None
        #print("BEFORE")
        #print(self.readyQ.qsize())
        while not self.readyQ.empty() and not hasWork:
            work = self.readyQ.get()
            if not work[1].equipment in worker.equipment_cert.split(", "):  #put in temp queue to cycle and look for good work
                temp.put(work)
            else: #work has been found
                while not temp.empty(): #put all the temporarily removed work back in the readyQ
                    self.readyQ.put(temp.get())
                self.readyQ.put(work) #adds the work back into the readyQ when found
                hasWork = True
            if self.readyQ.empty() and hasWork is False:
                while not temp.empty(): #put all the temporarily removed work back in the readyQ
                    self.readyQ.put(temp.get())
                #self.readyQ.put(work)
                break
        #print("AFTER")
        #print(self.readyQ.qsize())
        if hasWork is False:
            return None
        return work[1]
    #def get_equipment_list(self):
    #    return self.equipment_list
