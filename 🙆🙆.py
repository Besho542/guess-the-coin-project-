your_tasks = input("Enter your tasks fo today sebarated by comma: \n ").split(", ")

#نعمل مكتبه بقا عشان نخزن فيها الي اتعمل 

done_tasks = []
ongoing_tasks = []


for tasks in your_tasks :
    print(f"\n{tasks}\n")
    question = input(f"Did you finish {tasks} already: ").upper()
    if question == "YES" :
        print("Nice job")
        done_tasks.append(tasks)
    else:
        print("Try not to put it off")
        ongoing_tasks.append(tasks)
    print("----------")

#نطلع بقا من ال loop دي

done_today = input("(Do you want to see today's progress): (yes or no):   ").lower()
if done_today == "yes" : 
    print(f"""\n
                  ********** Done Tasks ***********
          
                    {done_tasks}


                  ********** Ongoing Tasks **********
                  
                    {ongoing_tasks}
""")
else:
    print("Press Enter to Finsh.....")
