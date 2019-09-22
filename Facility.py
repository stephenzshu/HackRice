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
        done = False
        removed = None
        temp = PriorityQueue()
        while self.activeQ.qsize() > 0:
            work = self.activeQ.get()
            if worker.current_task is work:   #might need 'is' operator or update the comparator
                temp.put(work)
            else:
                removed = work
                done = True
        while temp.qsize() > 0:
            self.activeQ.put(temp.get())
        return removed

    def getWork(self, worker):
        temp = PriorityQueue()
        hasWork = False
        work = None
        #print(self.name)
        while not self.readyQ.empty() and not hasWork:
            #print("loop")
            work = self.readyQ.get()
            if not work[1].equipment in worker.equipment_cert.split(", "):  #put in temp queue to cycle and look for good work
                temp.put(work)
            else: #work has been found
                while not temp.empty(): #put all the temporarily removed work back in the readyQ
                    self.readyQ.put(temp.get())
                self.activeQ.put(work)
                hasWork = True
            if self.readyQ.empty():
                while not temp.empty(): #put all the temporarily removed work back in the readyQ
                    self.readyQ.put(temp.get())
                self.readyQ.put(work)
                hasWork = True
        #print(self.readyQ.empty())
        #print(work)
        return work[1]

    def peekWork(self, worker):
        temp = PriorityQueue()
        hasWork = False
        work = None
        #print(self.readyQ.qsize())
        while not self.readyQ.empty() and not hasWork:
            work = self.readyQ.get()
            if not work[1].equipment in worker.equipment_cert.split(", "):  #put in temp queue to cycle and look for good work
                temp.put(work)
            else: #work has been found
                while not temp.empty(): #put all the temporarily removed work back in the readyQ
                    self.readyQ.put(temp.get())
                self.readyQ.put(work)
                hasWork = True
            if self.readyQ.empty():
                while not temp.empty(): #put all the temporarily removed work back in the readyQ
                    self.readyQ.put(temp.get())
                self.readyQ.put(work)
                hasWork = True
        #print(self.readyQ.qsize())

        return work[1]
    #def get_equipment_list(self):
    #    return self.equipment_list
