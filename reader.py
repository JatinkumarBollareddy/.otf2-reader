import otf2
import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter
from otf2.reader import *
from otf2.events import *
def two_scales(ax1,time1,data1,time2,data2):
    ax1.plot(time1, data1)
    ax1.plot(time2, data2)
    ax1.set_xlabel('Main LOOP')
    ax1.set_ylabel('Time')
    return ax1

def four_scales(ax1, time, data1, data2, data3, data4, c1, c2, c3, c4):
    ax2 = ax1.twinx()
    ax1.plot(time, data1, color=c1)
    ax1.plot(time, data3, color=c3)
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('Chunks per Joule (red) / Frequency (green)')
    ax1.legend(['CPJ','Frequence'], loc='upper left')
    ax2.plot(time, data2, color=c2)
    ax2.plot(time, data4, color=c4)
    ax2.set_ylabel('Temperature/core count')
    ax2.legend(['Temperature','Nb CPU'], loc='upper right')
    return ax1, ax2

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


cpu=[];m1=[];m3=[];m2=[];m4=[];m5=[];m6=[];m7=[];m_t=[];p=[];p_t=[];l=[];cpu_t=[];f=[];f_t=[];    #instantiating empty lists
with otf2.reader.open('/home/jatin/Documents/scorep-20180723_1503_576481374034/traces.otf2') as trace:
     for location, event in trace.events:


	if type(event).__name__== "Metric" :                         #extracting the metrics
		l= ("{}".format(event.metric))                       #output of event.metric ="Encountered Metric event {'attributes': None, 'metric': MetricInstance [2], 'values': [0], 'time': 384260495649L} on Location [4294967296] at time 384260495649"
		L=l.split(":")
		if L[0]=="MetricInstance [8]":
			cpu.append((event.values[0])/1000.0)         #the number of if,elif conditions will depend on number of different  metric recorded in the trace file.
			cpu_t.append(int(event.time))
		elif L[0]=="MetricInstance [4]":                     #the metrics are segregated into their respective lists based on the MetricInstance
			f.append((event.values[0]))
			f_t.append(int(event.time))                  #the method to know the MetricInstance of a metric is discussed in the Readme file
		elif L[0]=="MetricInstance [6]":
			p.append((event.values[0])/100.0)
			p_t.append(int(event.time))
		elif L[0]=="MetricClass [0]":                        #the synchronous metrics (papi and perf metrics selected in the eviranment variable)
			m1.append((event.values[0])); m2.append((event.values[1]));m3.append((event.values[2]));m4.append((event.values[3])); m5.append((event.values[4]));m6.append((event.values[5])); 
			m_t.append(int(event.time))
      
m_t=np.array(m_t); m1=np.array(m1); cpu=np.array(cpu); m2=np.array(m2); m3=np.array(m3); m4=np.array(m4); m5=np.array(m5); m6=np.array(m6); m7=np.array(m7);
cpu_t=np.array(cpu_t); p_t=np.array(p_t); p=np.array(p); f=np.array(f);     f_t=np.array(f_t);      #the arrays are converted into the numpy arrays

fig, ax = plt.subplots(figsize=(20, 10))                                                         #plotting 
#ax1,ax2=four_scales(ax,cpu_t,smooth(cpu,2),p_t,smooth(p,2),m_t,m4,m_t,m5,'r', 'b', 'g', 'k')
#plt.plot(f_t,f)
#plt.show()
ax1,ax2=three_scales(ax,cpu_t,smooth(cpu,2),p_t,smooth(p,2),f_t,smooth(f,1),'r', 'b', 'g')


fig, ax3 = plt.subplots(figsize=(20, 10))
ax4 = ax3.twinx()
ax3.plot(m_t,smooth(m1,3))
ax3.plot(m_t,smooth(m2,2))
ax3.plot(m_t,smooth(m3,2))
plt.xlim(p_t[0],p_t[len(p_t)-1])
ax3.set_xlabel('time stamp')
ax3.set_ylabel('Level 2-load misses,Data Cache misses, Store misses')
ax3.legend(['load misses','Data Cache misses',' Store misses'], loc='upper left')

ax4.plot(m_t, m4,color='c')
ax4.plot(m_t, m5, color='k')
ax4.set_ylabel('No. Cycles /Instructions')
ax4.legend(['No. Cycles','Instructions'], loc='lower right')

plt.show()

workbook = xlsxwriter.Workbook('Experiment4.xlsx')            #an optional step if we want to export the metrics as an excel file
worksheet = workbook.add_worksheet()

worksheet.write_row('A1', ('Timestamp','m1', 'm2', 'm3', 'Page-faults', '', 'CPU-cycles','','Time stamp','CPU temperature (C)','','Time stamp','CPU Power Consumed (W)'))
worksheet.write_column('A2',m_t); worksheet.write_column('B2',m1); worksheet.write_column('C2',m2);worksheet.write_column('D2',m3);worksheet.write_column('E2',m4); worksheet.write_column('G2',m6);worksheet.write_column('I2',cpu_t);worksheet.write_column('J2',cpu);worksheet.write_column('L2',p_t);worksheet.write_column('M2',p);



workbook.close()
