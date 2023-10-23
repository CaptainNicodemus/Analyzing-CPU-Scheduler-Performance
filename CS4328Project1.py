#Nicodemus Robles 10/20/2023

import numpy as np
import heapq
import csv

global hrrnaverage_turnaround_time, hrrntotal_wait_time, hrrntotal_time
global SRTFaverage_turnaround_time, SRTFtotal_wait_time, SRTFtotal_time
global RRaverage_turnaround_time, RRtotal_wait_time, RRtotal_time


class SJF:


    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = i

            arrival_time = arrival_times[i]

            burst_time = service_times[i]

        

            temporary.extend([process_id, arrival_time, burst_time, 0])
            '''
            '0' is the state of the process. 0 means not executed and 1 means execution complete
            '''
            process_data.append(temporary)
        SJF.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_processes = []
        '''
        Sort processes according to the Arrival Time
        '''
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    response_ratio = 0
                    response_ratio = float(((s_time - process_data[j][1]) + process_data[j][2]) / process_data[j][2])
                    '''
                    Calculating the Response Ratio foe each process
                    '''
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], response_ratio])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2], reverse=True)
                '''
                Sort the processes according to the Highest Response Ratio
                '''
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_processes.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_processes.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
        t_time = SJF.calculateTurnaroundTime(self, process_data)
        w_time = SJF.calculateWaitingTime(self, process_data)

        SJF.printData(self, process_data, t_time, w_time, sequence_of_processes)

    def calculateTurnaroundTime(self, process_data):
        global SRTFaverage_turnaround_time, SRTFtotal_time
        total_turnaround_time = 0
        SRTFtotal_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
            if SRTFtotal_time < process_data[i][4]:
                SRTFtotal_time = process_data[i][4]
        
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        
        
        SRTFaverage_turnaround_time = average_turnaround_time
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        waiting_times = []
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]
            waiting_times.append(waiting_time)
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        global SRTFtotal_wait_time
        SRTFtotal_wait_time = total_waiting_time
        '''
        average_waiting_time = total_waiting_time / no_of_processes
        '''
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_processes):
        process_data.sort(key=lambda x: x[0])

      
        '''
        Sort processes according to the Process ID
        '''

        '''
        print("Process_ID  Arrival_Time  Burst_Time      Completed  Completion_Time  Turnaround_Time  Waiting_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j])
            print()
        
     

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')

        print(f'Sequence of Processes: {sequence_of_processes}')
        '''
       
class HRRN:


    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = i

            arrival_time = arrival_times[i]

            burst_time = service_times[i]

        

            temporary.extend([process_id, arrival_time, burst_time, 0])
            '''
            '0' is the state of the process. 0 means not executed and 1 means execution complete
            '''
            process_data.append(temporary)
        HRRN.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_processes = []
        '''
        Sort processes according to the Arrival Time
        '''
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    response_ratio = 0
                    response_ratio = float(((s_time - process_data[j][1]) + process_data[j][2]) / process_data[j][2])
                    '''
                    Calculating the Response Ratio foe each process
                    '''
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], response_ratio])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=True)
                '''
                Sort the processes according to the Highest Response Ratio
                '''
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_processes.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_processes.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
        t_time = HRRN.calculateTurnaroundTime(self, process_data)
        w_time = HRRN.calculateWaitingTime(self, process_data)

        HRRN.printData(self, process_data, t_time, w_time, sequence_of_processes)

    def calculateTurnaroundTime(self, process_data):
        global hrrnaverage_turnaround_time, hrrntotal_time
        total_turnaround_time = 0
        hrrntotal_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
            if hrrntotal_time < process_data[i][4]:
                hrrntotal_time = process_data[i][4]
        
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        
        
        hrrnaverage_turnaround_time = average_turnaround_time
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        waiting_times = []
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]
            waiting_times.append(waiting_time)
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        global hrrntotal_wait_time
        hrrntotal_wait_time = total_waiting_time
        '''
        average_waiting_time = total_waiting_time / no_of_processes
        '''
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_processes):
        process_data.sort(key=lambda x: x[0])

      
        '''
        Sort processes according to the Process ID
        '''

        '''
        print("Process_ID  Arrival_Time  Burst_Time      Completed  Completion_Time  Turnaround_Time  Waiting_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j])
            print()
        
     

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')

        print(f'Sequence of Processes: {sequence_of_processes}')

        
        '''

class RoundRobin:

    def processData(self, no_of_processes,timeS):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = i

            arrival_time = arrival_times[i]

            burst_time = service_times[i]

            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            '''
            '0' is the state of the process. 0 means not executed and 1 means execution complete
            
            '''
            process_data.append(temporary)

        time_slice =  timeS

        RoundRobin.schedulingProcess(self, process_data, time_slice)

    def schedulingProcess(self, process_data, time_slice):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        while 1:
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1
                    '''
                    The above if loop checks that the next process is not a part of ready_queue
                    '''
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    '''
                    The above if loop adds a process to the ready_queue only if it is not already present in it
                    '''
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                    '''
                    The above if loop makes sure that the recently executed process is appended at the end of ready_queue
                    '''
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                if ready_queue[0][2] > time_slice:
                    '''
                    If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    '''
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= time_slice:
                    '''
                    If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    '''
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                if normal_queue[0][2] > time_slice:
                    '''
                    If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    '''
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                elif normal_queue[0][2] <= time_slice:
                    '''
                    If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    '''
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)



        t_time = RoundRobin.calculateTurnaroundTime(self, process_data)
        w_time = RoundRobin.calculateWaitingTime(self, process_data)
        RoundRobin.printData(self, process_data, t_time, w_time, executed_process)

    def calculateTurnaroundTime(self, process_data):
        global rraverage_turnaround_time, rrtotal_time
        total_turnaround_time = 0
        rrtotal_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)

            
            if rrtotal_time < process_data[i][5]:
                rrtotal_time = process_data[i][5]
        
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        
        
        rraverage_turnaround_time = average_turnaround_time
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        average_waiting_time = total_waiting_time / no_of_processes

        '''
        global rrtotal_wait_time
        rrtotal_wait_time = total_waiting_time
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, executed_process):
        process_data.sort(key=lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        '''
        print("Process_ID  Arrival_Time  Rem_Burst_Time   Completed  Original_Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j], end="				")
            print()

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')

        print(f'Sequence of Processes: {executed_process}')

        '''











def sortByArrival(at, n):
     
    # Selection Sort applied  
    for i in range(0, n - 1):
        for j in range(i + 1, n):
             
            # Check for lesser arrival time  
            if at[i] > at[j]:
                 
                # Swap earlier process to front
                at[i], at[j] = at[j], at[i]

def fcfs(arrival_times, service_times):
    if not arrival_times or not service_times or len(arrival_times) != len(service_times):
        return None  # Invalid input

    n = len(arrival_times)
    completion_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n

    for i in range(n):
        if i == 0:
            completion_times[i] = arrival_times[i] + service_times[i]
        else:
            completion_times[i] = max(arrival_times[i], completion_times[i - 1]) + service_times[i]

        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - service_times[i]


    return {
        "completion_times": completion_times,
        "turnaround_times": turnaround_times,
        "waiting_times": waiting_times,
    }

def add_row_to_csv(file_path, data):
    """
    Add a row to a CSV file.

    Args:
        file_path (str): The path to the CSV file.
        data (list): The list of data for the new row.
    """
    # Check if the file already exists or not
    file_exists = False
    try:
        with open(file_path, 'r', newline='') as csvfile:
            file_exists = True
    except FileNotFoundError:
        pass

    # Open the CSV file in append mode
    with open(file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # If the file is newly created, write the header row
        if not file_exists:
            # Assuming the first row should be the header row
            header = [f"Column_{i + 1}" for i in range(len(data))]
            csv_writer.writerow(header)

        # Write the new row of data
        csv_writer.writerow(data)

def running(arrival_rate_values):

    print()
    print()
    print("fcfs")
    print()
    result = fcfs(arrival_times, service_times)
    avgTurnTime = 0
    endTime = 0
    tottalServiceTime = 0
    avgReady = 0
    if result:
        #print("Process\tArrival Time\tService Time\tCompletion Time\tTurnaround Time\tWaiting Time")
        
        for i in range(len(arrival_times)):

            #print(f"P{i + 1}\t{arrival_times[i]}\t\t{service_times[i]}\t\t{result['completion_times'][i]}\t\t{result['turnaround_times'][i]}\t\t{result['waiting_times'][i]}")
            
            avgTurnTime += result['turnaround_times'][i]
            tottalServiceTime += service_times[i]
            if endTime < result['completion_times'][i]:
                endTime = result['completion_times'][i]
    


    total_wait_time = sum(result['waiting_times'])

    print(endTime)
    print(tottalServiceTime)
    print(total_wait_time)


    cpuUtilizationTime = tottalServiceTime / endTime
    

    average_queue_size = total_wait_time / total_processes
    totalThroughput = total_processes / endTime
    avgTurnTime = avgTurnTime /  total_processes

    print(f"Average turnaround time:                        {avgTurnTime}")
    print(f"The total throughput:                           {totalThroughput}")
    print(f"CPU utilization:                                {cpuUtilizationTime}%")
    print(f"Average number of processes in the ready queue: {average_queue_size}")
    
    data_to_add = ["fcfs",arrival_rate_values, avgTurnTime, totalThroughput,cpuUtilizationTime,average_queue_size]
    add_row_to_csv("runData.csv", data_to_add)

    
    
    
    
    
    
    print()
    print()
    print("SRTF")
    print()
    sjf = SJF()
    sjf.processData(total_processes)
    print(SRTFtotal_time)
    print(tottalServiceTime)
    print(SRTFtotal_wait_time)

    cpuUtilizationTime = tottalServiceTime / SRTFtotal_time
    
    
    average_queue_size = SRTFtotal_wait_time / total_processes
    totalThroughput = total_processes / SRTFtotal_time
    avgTurnTime = SRTFaverage_turnaround_time

    print(f"Average turnaround time:                        {avgTurnTime}")
    print(f"The total throughput:                           {totalThroughput}")
    print(f"CPU utilization:                                {cpuUtilizationTime}%")
    print(f"Average number of processes in the ready queue: {average_queue_size}")

    data_to_add = ["SRTF",arrival_rate_values, avgTurnTime, totalThroughput,cpuUtilizationTime,average_queue_size]
    add_row_to_csv("runData.csv", data_to_add)






    print()
    print()
    print("hrrn_scheduling")
    print()
    hrrn = HRRN()
    hrrn.processData(total_processes)
    
    print(hrrntotal_time)
    print(tottalServiceTime)
    print(hrrntotal_wait_time)

    cpuUtilizationTime = tottalServiceTime / hrrntotal_time
    
    
    average_queue_size = hrrntotal_wait_time / total_processes
    totalThroughput = total_processes / hrrntotal_time
    avgTurnTime = hrrnaverage_turnaround_time

    print(f"Average turnaround time:                        {avgTurnTime}")
    print(f"The total throughput:                           {totalThroughput}")
    print(f"CPU utilization:                                {cpuUtilizationTime}%")
    print(f"Average number of processes in the ready queue: {average_queue_size}")
    
    data_to_add = ["hrrn_scheduling",arrival_rate_values, avgTurnTime, totalThroughput,cpuUtilizationTime,average_queue_size]
    add_row_to_csv("runData.csv", data_to_add)







    print()
    print()
    print("RoundRobin 0.01")
    print()
    rr = RoundRobin()
    rr.processData(total_processes,0.01)
    print(rrtotal_time)
    print(tottalServiceTime)
    print(rrtotal_wait_time)

    cpuUtilizationTime = tottalServiceTime / hrrntotal_time
    
    
    average_queue_size = rrtotal_wait_time / total_processes
    totalThroughput = total_processes / rrtotal_time
    avgTurnTime = rraverage_turnaround_time

    print(f"Average turnaround time:                        {avgTurnTime}")
    print(f"The total throughput:                           {totalThroughput}")
    print(f"CPU utilization:                                {cpuUtilizationTime}%")
    print(f"Average number of processes in the ready queue: {average_queue_size}")

    data_to_add = ["RoundRobin 0.01",arrival_rate_values, avgTurnTime, totalThroughput,cpuUtilizationTime,average_queue_size]
    add_row_to_csv("runData.csv", data_to_add)









    print()
    print()
    print("RoundRobin 0.2")
    print()
    rr = RoundRobin()
    rr.processData(total_processes,0.2)
    
    print(rrtotal_time)
    print(tottalServiceTime)
    print(rrtotal_wait_time)


    cpuUtilizationTime = tottalServiceTime / hrrntotal_time
    
    
    average_queue_size = rrtotal_wait_time / total_processes
    totalThroughput = total_processes / rrtotal_time
    avgTurnTime = rraverage_turnaround_time
    print(f"Average turnaround time:                        {avgTurnTime}")
    print(f"The total throughput:                           {totalThroughput}")
    print(f"CPU utilization:                                {cpuUtilizationTime}%")
    print(f"Average number of processes in the ready queue: {average_queue_size}")

    data_to_add = ["RoundRobin 0.2",arrival_rate_values, avgTurnTime, totalThroughput,cpuUtilizationTime,average_queue_size]
    add_row_to_csv("runData.csv", data_to_add)



# usage:
if __name__ == "__main__":


    # Define simulation parameters
    total_processes = 10000

    average_service_time = 0.06  
    arrival_rate_values = 30  # Vary λ to simulate different loads




    # Initialize lists to store process arrival times and service times
    # Simulation loop
    time = 0
    arrival_times = []
    service_times = []

    for x in range(total_processes):
        # Generate the arrival time based on a Poisson process
        arrival_time = np.random.exponential(1 / arrival_rate_values)



        time += arrival_time
        arrival_times.append(time)

        # Generate the service time based on an exponential distribution
        service_time = np.random.exponential(average_service_time)

        service_times.append(service_time)
    
    i = 0
    while i < 30:
        
        i += 1
        running(i)

    





    



















  








