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

    def getWork(self, worker):
        temp = PriorityQueue()
        hasWork = False
        work = 0
        while not hasWork:
            work = readyQ.get()
            if not work.equipment in worker.equipment_cert  #put in temp queue to cycle and look for good work
                temp.put(work)
            else: #work has been found
                while not temp.empty(): #put all the temporarily removed work back in the readyQ
                    readyQ.put(temp.get())
                activeQ.put(work)
                hasWork = True
        return work
    #def get_equipment_list(self):
    #    return self.equipment_list
