import time
from datetime import date,datetime
#Add your date in the variable b
#Output will be in the format ('11 Years', '0 Months', '9 Days')
def convertSeconds(seconds):
    y_tmp = round(seconds/60/60/24/365.25,3)
    y=round(y_tmp)
    m_tmp = (y_tmp*12  - y*12)
    m=round(m_tmp)
    d_tmp = (y_tmp*12  - y*12)*30
    d=round(d_tmp)
    return str(y)+" Years", str(m)+" Months", str(d)+" Days"

a=datetime.today().date()
b=date(2008,7,28)
c=(a - b)
seconds=c.total_seconds()
print(convertSeconds(seconds))
