class Time:
    def __init__(self,hh,mm,ss):
        self.hour = hh
        self.min = mm
        self.sec = ss
        self.fix()

    def show(self):
        print(self.hour,":",self.min,":",self.sec)

    def sum(self, other):
        new_sec = self.sec + other.sec
        new_min = self.min + other.min
        new_hour = self.hour + other.hour
        result = Time(new_hour, new_min, new_sec)
        return result

    def sub(self,other):
        new_sec = self.sec - other.sec
        new_min = self.min - other.min
        new_hour = self.hour - other.hour
        result = Time(new_hour, new_min, new_sec)
        return result
    
    def time_to_sec(self):
        result = (self.hour * 60 + self.min) * 60 + self.sec
        return result
    
    def sec_to_time(second,hour,min):
        new_hour = second // 3600
        new_min = (second - hour * 3600) // 60
        new_sec = (second - hour * 3600) - min * 60
        result = Time(new_hour, new_min, new_sec)
        return result
        
    def gmt_to_tehran(self):
        tehran_time = Time(3, 30, 0)
        result = self.sum(tehran_time)
        return result

    def fix(self):
        if self.sec >= 60:
            while True:
                if self.sec >= 60:
                    self.sec -= 60
                    self.min += 1
                else:
                    break
        if self.min>=60:
            while True:
                if self.min >= 60:
                    self.min -= 60
                    self.hour += 1
                else:
                    break
        if self.sec < 0:
            while True:
                if self.sec < 0:
                    self.sec += 60
                    self.min -= 1
                else:
                    break
        if self.min < 0:
            while True:
                if self.min < 0:
                    self.min += 60
                    self.hour -= 1
                else:
                    break




t1=Time(5,42,25)
t2=Time(2,14,56)

t1.show()
t2.show()

s1=t1.sum(t2)
s1.show()

s2=t1.sub(t2)
s2.show()

sec=t1.time_to_sec()
print(sec)

G=Time(14,35,8)
I=G.gmt_to_tehran()
I.show()
