""" 
django server send task to be performed by celery worker, even those 
task not finished, django send the responce back to user immediately
that task was received.

A task queue's input is unit of work called a task. Dedicated worker 
processes constantly monitor task queues for new work to perform.

Celery beat send task on schedule to broker, then broker send it to 
celery worker, then worker call third party Api and retrieve call back.

Why to use celery?
Third party Api Calls
For high CPU intensive tasks
Periodic/sheduled tasks
For improving user experience

Multithreading - when django server gives task to celery worker
cronjob - for light sheduled tasks
Django celery results - to store information, and we can see it in 
django admin

Celery system can consist of multiple workers and brokers, giving way
to high availability and horizontal scaling

Worker
When you start a Celery worker on the command line via celery-app=..., 
you just start a supervisor process. The Celery worker itself does not
process any tasks. It spawns child processes(or threads) for concurrency 
and deals with all the book keeping stuff. The child processes(or threads) 
execute the actual tasks. These child processes(or threads) are also 
known as the execution pool. 
The size of the execution pool determines the number of tasks your
Celery worker can process in one single time - equals to the number of
child processes(or threads). And also it depends on how many cores 
(CPU) your system has. So number of tasks=quantity of CPU cores
Multiprocessing - celery spawns child processes(or threads).

Pool - decides who will actually perform the tasks - thread, child
process, worker itself or else.
CPU based task allocated to child process.
I/O based task - to thread
"""