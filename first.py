__author__ = 'dhs'
import re
import copy

class GoodTime(object):
    def __init__(self):
        self.max_min = [{'max':0,'min':0},{'max':0,'min':0},{'max':0,'min':0},{'max':0,'min':0}]
        self.diff = [[],[],[],[]]
        self.count = [0,0,0,0]
        self.current_state = [0,0,0,0]
        self.bef_state=[]

    def state(self,num,j):
        if num < 0:
            self.current_state[j] = 0
        else:
            self.current_state[j] = 1
        #print 'state ok'

    def getmaxmin(self,num,j):
        if num > self.max_min[j]['max']:
            self.max_min[j]['max'] = num
        if num < self.max_min[j]['min']:
            self.max_min[j]['min'] = num
        #print 'maxmin over'

    def main(self,file):
        pattern = re.compile(r'\s+')
        with open(file,'r') as f:
            for i in f.readlines():
                numlist = re.sub(pattern,' ',i.strip()).split(' ')
                #print numlist
                j = 0
                while j < 4:
                    self.state(float(numlist[j]),j)
                    j+=1
                # print self.current_state
                if len(self.bef_state) == 0:
                    self.bef_state = copy.deepcopy(self.current_state)
                k = 0
                while k < 4:
                    if self.current_state[k] != self.bef_state[k]:
                        self.count[k]+=1
                    if self.count[k] == 2:
                        #if k ==0 :
                           # print numlist
                        self.diff[k].append(self.max_min[k]['max']-self.max_min[k]['min'])
                        self.max_min[k] = {'max':0,'min':0}
                        self.getmaxmin(float(numlist[k]),k)
                        self.count[k] = 0
                    else:
                        self.getmaxmin(float(numlist[k]),k)
                    k+=1
                self.bef_state = copy.deepcopy(self.current_state)
            count = 0
            while count < 4:
                if self.count[count] == 1:
                    self.diff[count].append(self.max_min[count]['max']-self.max_min[count]['min'])
                count+=1
        if file == './10B':
            print file.split('/')[1]
            for item in self.diff:
                item.sort()
                newitem = item[(int(len(item)*2)/3):]

                print "%.6f"%(float(sum(newitem))/float(len(newitem)))
        else:
           print file.split('/')[1]
           for item in self.diff:
               print "%.6f"%(float(sum(item))/float(len(item)))


if __name__ == '__main__':
    r = GoodTime()
    r.main('./10A')
    r.main('./10B')
