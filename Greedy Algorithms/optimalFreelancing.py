def priority(job) :
    return (job["deadline"]*10000 + (100-job["payment"]))

def optimalFreelancing(jobs):
    # Write your code here.
    jobs.sort(key=priority)
    day = 1
    ans = 0
    ignoredJobs = []
    takenJobs = []
    while jobs and (day != 8) :
        job = jobs.pop(0)
        if job["deadline"] < day :
            ignoredJobs.append(job)
            continue
        takenJobs.append(job)
        day += 1
    for ijob in ignoredJobs :
        for j in range(0,ijob["deadline"]) :
            if takenJobs[j]["payment"] < ijob["payment"] :
                takenJobs[j] = ijob
                print(ijob,"\n",takenJobs)
    ans = 0
    for job in takenJobs :
        ans += job["payment"]
    return ans
