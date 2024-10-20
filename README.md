CPU Scheduling Algorithms 

Hey there, genius. You've just stepped into a world where CPU scheduling meets slick, next-gen user interfaces. This application—yeah, this one—lets you visualize how CPU scheduling algorithms work in real time. You know, the algorithms your processors rely on to handle multitasking and keep everything from crashing. Welcome to my world.
Features (or as I call them, "Perks")

1.	Multiple Algorithms:
o	Round Robin (RR): Fast, fair, and just like me, doesn’t like to wait. Time quantum's the secret sauce here.
o	Shortest Job First (SJF): Think efficiency. We take the shortest task and tackle it head-on.
o	Priority Scheduling: If you're important, you go first. Pretty much like how I live.
o	First Come First Serve (FCFS): The old-fashioned queue method. Whoever arrives first gets my attention.

3.	Process Input:
o	Add in processes with burst times, arrival times, and priorities (because not all processes are equal—like me, always top priority).
o	Define a time quantum for Round Robin, because a genius loves to tinker with time.

5.	Visual Output:
o	Four tabs, one for each algorithm. Check out the completion times, turnaround times, and wait times. Want details? You got 'em.
o	You’ll see beautifully plotted time bars that give you a clear picture of how each scheduling algorithm handles your processes—right there on the screen.

7.	Dynamic Gantt Chart:
o	Real-time Gantt chart plotting. Yeah, we’re going full visual. You’ll see how each process gets its time in the spotlight, broken down by algorithm. Eye candy for tech brains.
Setup and Launch

How to Fire This Baby Up:
1.	Dependencies: Make sure you've got Tkinter, Matplotlib, and ttk running in your Python environment. It’s not rocket science... oh wait, I do that too.
bash

pip install matplotlib
2.	Running the Application:
o	Clone the repo or drop the script into your Python environment.
o	Then simply run:
bash

python cpu_scheduler.py
o	And voilà, the interface pops up. You can now input processes, set burst times, priorities, arrival times—everything you'd need to simulate scheduling algorithms.

3.	Input Format:
o	Number of Processes: Straight number. Like how many times I've saved the planet.
o	Burst Times: Comma-separated integers (e.g., 5, 3, 8, 6).
o	Arrival Times: Same as burst times (because even in simulations, timing matters).
o	Priorities: Comma-separated (give some love to those high-priority tasks).
o	Time Quantum: Enter a value, especially if you're into Round Robin. You’ll know when you’ve got it right.


Technical Notes (because details matter)

•	Class Design: We’ve got a Process class that defines each process—burst time, arrival time, priority, and the whole shebang. Just like how I define my suits.
•	Algorithm Implementations: Algorithms are designed to simulate real-world CPU scheduling. You’ll see how they each compute completion, turnaround, and waiting times.
•	UI/UX: A sleek interface built with Tkinter and ttk. Let’s be honest, anything less would be embarrassing.

![image](https://github.com/user-attachments/assets/652d1949-0f89-457a-9bfd-43d53d473db0)

![image](https://github.com/user-attachments/assets/04576e3a-64bb-4744-9142-bffda2f5cf37)

![image](https://github.com/user-attachments/assets/20bcf2e6-53e8-4e75-a938-97d1aa841eb8)

![image](https://github.com/user-attachments/assets/a43da624-634d-4eef-8adb-abf7e6971040)




Why This Matters
Maybe you’re studying computer science, maybe you're trying to optimize CPU performance, or maybe you’re just a curious mind who appreciates efficient multitasking. In any case, this app shows how processes are scheduled in your CPU, with real-time feedback and visuals that’ll make any tech geek happy.
Now go ahead, launch it, and feel like a scheduling genius. Just try to keep up.

