import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class Process:
    def __init__(self, pid, burst_time, arrival_time=0, priority=0):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


class SchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduling Algorithms")

        # Inputs
        self.process_frame = ttk.LabelFrame(root, text="Process Input")
        self.process_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.num_processes_label = ttk.Label(self.process_frame, text="Number of Processes:")
        self.num_processes_label.grid(row=0, column=0)
        self.num_processes_entry = ttk.Entry(self.process_frame)
        self.num_processes_entry.grid(row=0, column=1)

        self.burst_time_label = ttk.Label(self.process_frame, text="Burst Times (comma separated):")
        self.burst_time_label.grid(row=1, column=0)
        self.burst_time_entry = ttk.Entry(self.process_frame)
        self.burst_time_entry.grid(row=1, column=1)

        self.arrival_time_label = ttk.Label(self.process_frame, text="Arrival Times (comma separated):")
        self.arrival_time_label.grid(row=2, column=0)
        self.arrival_time_entry = ttk.Entry(self.process_frame)
        self.arrival_time_entry.grid(row=2, column=1)

        self.priority_label = ttk.Label(self.process_frame, text="Priorities (comma separated):")
        self.priority_label.grid(row=3, column=0)
        self.priority_entry = ttk.Entry(self.process_frame)
        self.priority_entry.grid(row=3, column=1)

        self.time_quantum_label = ttk.Label(self.process_frame, text="Time Quantum for RR:")
        self.time_quantum_label.grid(row=4, column=0)
        self.time_quantum_entry = ttk.Entry(self.process_frame)
        self.time_quantum_entry.grid(row=4, column=1)

        self.schedule_button = ttk.Button(self.process_frame, text="Schedule", command=self.schedule_processes)
        self.schedule_button.grid(row=5, columnspan=2)

        # Output Frame with Tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Creating tabs for each scheduling algorithm
        self.tabs = {
            "Round Robin": self.create_output_tab(),
            "Shortest Job First": self.create_output_tab(),
            "Priority Scheduling": self.create_output_tab(),
            "First Come First Serve": self.create_output_tab()
        }

        for tab_name, tab in self.tabs.items():
            self.notebook.add(tab, text=tab_name)

    def create_output_tab(self):
        tab = ttk.Frame(self.notebook)
        table = ttk.Treeview(tab, columns=("Process", "Arrival", "Burst", "Completion", "Turnaround", "Waiting"), show='headings')
        table.heading("Process", text="Process")
        table.heading("Arrival", text="Arrival Time")
        table.heading("Burst", text="Burst Time")
        table.heading("Completion", text="Completion Time")
        table.heading("Turnaround", text="Turnaround Time")
        table.heading("Waiting", text="Waiting Time")
        table.grid(row=0, column=0, sticky="nsew")
        
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        return tab

    def schedule_processes(self):
        self.clear_tables()
        
        try:
            num_processes = int(self.num_processes_entry.get())
            burst_times = list(map(int, self.burst_time_entry.get().split(',')))
            arrival_times = list(map(int, self.arrival_time_entry.get().split(',')))
            priorities = list(map(int, self.priority_entry.get().split(',')))
            time_quantum = int(self.time_quantum_entry.get())
            
            processes = [Process(i + 1, burst_times[i], arrival_times[i], priorities[i]) for i in range(num_processes)]
            
            rr_time_bar = self.round_robin(processes.copy(), time_quantum)
            self.update_table(self.tabs["Round Robin"], processes)

            sjf_time_bar = self.sjf(processes.copy())
            self.update_table(self.tabs["Shortest Job First"], processes)

            ps_time_bar = self.priority_scheduling(processes.copy())
            self.update_table(self.tabs["Priority Scheduling"], processes)

            fcfs_time_bar = self.fcfs(processes.copy())
            self.update_table(self.tabs["First Come First Serve"], processes)

            self.plot_time_bars(rr_time_bar, sjf_time_bar, ps_time_bar, fcfs_time_bar)
            
        except Exception as e:
            print(f"Error: {e}")

    def round_robin(self, processes, time_quantum):
        time = 0
        remaining_burst = [p.burst_time for p in processes]
        time_bar = []

        while True:
            all_done = True
            for i in range(len(processes)):
                if remaining_burst[i] > 0:
                    all_done = False
                    if remaining_burst[i] > time_quantum:
                        time += time_quantum
                        remaining_burst[i] -= time_quantum
                        time_bar.append((time - time_quantum, time, processes[i].pid))
                    else:
                        time += remaining_burst[i]
                        time_bar.append((time - remaining_burst[i], time, processes[i].pid))
                        remaining_burst[i] = 0
                        processes[i].completion_time = time

            if all_done:
                break

        # Calculate turnaround and waiting times
        for p in processes:
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time

        return time_bar

    def sjf(self, processes):
        time = 0
        processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
        time_bar = []

        for p in processes:
            if time < p.arrival_time:
                time = p.arrival_time
            time += p.burst_time
            p.completion_time = time
            time_bar.append((time - p.burst_time, time, p.pid))

        # Calculate turnaround and waiting times
        for p in processes:
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time

        return time_bar

    def priority_scheduling(self, processes):
        time = 0
        processes.sort(key=lambda x: (x.arrival_time, x.priority))
        time_bar = []

        for p in processes:
            if time < p.arrival_time:
                time = p.arrival_time
            time += p.burst_time
            p.completion_time = time
            time_bar.append((time - p.burst_time, time, p.pid))

        # Calculate turnaround and waiting times
        for p in processes:
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time

        return time_bar

    def fcfs(self, processes):
        time = 0
        processes.sort(key=lambda x: x.arrival_time)
        time_bar = []

        for p in processes:
            if time < p.arrival_time:
                time = p.arrival_time
            time += p.burst_time
            p.completion_time = time
            time_bar.append((time - p.burst_time, time, p.pid))

        # Calculate turnaround and waiting times
        for p in processes:
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time

        return time_bar

    def plot_time_bars(self, rr_time_bar, sjf_time_bar, ps_time_bar, fcfs_time_bar):
        fig, ax = plt.subplots(figsize=(10, 4))

        # Prepare data for plotting
        for start, end, pid in rr_time_bar:
            ax.barh(y=1, width=end-start, left=start, color='cyan', edgecolor='black')
            ax.text((start + end) / 2, 1, f'P{pid}', va='center', ha='center', color='black')

        for start, end, pid in sjf_time_bar:
            ax.barh(y=2, width=end-start, left=start, color='salmon', edgecolor='black')
            ax.text((start + end) / 2, 2, f'P{pid}', va='center', ha='center', color='black')

        for start, end, pid in ps_time_bar:
            ax.barh(y=3, width=end-start, left=start, color='lightgreen', edgecolor='black')
            ax.text((start + end) / 2, 3, f'P{pid}', va='center', ha='center', color='black')

        for start, end, pid in fcfs_time_bar:
            ax.barh(y=4, width=end-start, left=start, color='lightblue', edgecolor='black')
            ax.text((start + end) / 2, 4, f'P{pid}', va='center', ha='center', color='black')

        ax.set_yticks([1, 2, 3, 4])
        ax.set_yticklabels(['Round Robin', 'SJF', 'Priority Scheduling', 'FCFS'])
        ax.set_xlabel('Time')
        ax.set_title('CPU Scheduling Time Bars')

        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=2, column=0, sticky="nsew")
        self.canvas.draw()

    def clear_tables(self):
        for tab_name in self.tabs.keys():
            table = self.tabs[tab_name].children['!treeview']
            for item in table.get_children():
                table.delete(item)

    def update_table(self, tab, processes):
        table = tab.children['!treeview']
        for p in processes:
            table.insert("", "end", values=(p.pid, p.arrival_time, p.burst_time, p.completion_time, p.turnaround_time, p.waiting_time))


if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerGUI(root)
    root.mainloop()
