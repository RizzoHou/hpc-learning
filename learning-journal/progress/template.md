# Progress Tracking Template

Use this template to track your daily learning progress and set weekly goals.

## Daily Log

### Date: [YYYY-MM-DD]

#### Today's Focus
- [ ] Module: [Which module are you working on?]
- [ ] Concept: [Specific concept or topic]
- [ ] Exercise: [Exercise or project]

#### Time Spent
- Start time: [HH:MM]
- End time: [HH:MM]
- Total time: [X hours Y minutes]

#### What I Learned Today
- [Brief summary of key learnings]
- [New concepts understood]
- [Skills practiced]

#### Code/Experiments
```[language]
[Code snippets or commands tried]
```

#### Output/Results
```
[Output from running code or experiments]
```

#### Challenges Faced
- [Specific problems encountered]
- [Error messages received]
- [What didn't work as expected]

#### Solutions Found
- [How you solved the challenges]
- [Resources that helped (documentation, forums, etc.)]
- [Key insights gained]

#### Questions for Future Exploration
- [Questions that came up during learning]
- [Topics to research further]
- [Experiments to try next]

#### Mood/Reflection
- [How you felt about today's learning]
- [What was most rewarding]
- [What was most frustrating]

---

## Weekly Summary

### Week: [Week Number, e.g., Week 1]

#### Goals for This Week
- [ ] [Specific goal 1]
- [ ] [Specific goal 2]
- [ ] [Specific goal 3]

#### Progress This Week
- Modules completed: [List]
- Exercises solved: [Number and types]
- Projects started/completed: [Details]
- Key skills developed: [List]

#### Time Investment
- Total hours this week: [X]
- Most productive day: [Day and hours]
- Consistency rating: [1-5 scale]

#### Biggest Achievement
[Most significant learning or accomplishment]

#### Biggest Challenge
[Most difficult obstacle faced]

#### Key Insights
1. [Insight 1]
2. [Insight 2]
3. [Insight 3]

#### Next Week's Goals
1. [Goal 1]
2. [Goal 2]
3. [Goal 3]

#### Adjustments to Learning Approach
[Changes you'll make based on this week's experience]

---

## Monthly Review

### Month: [Month Year]

#### Overall Progress
- Modules completed: [X/Y]
- Exercises solved: [Number]
- Projects completed: [Number]
- Total learning hours: [X]

#### Skill Development
- New skills acquired: [List]
- Skills improved: [List]
- Skills to focus on next month: [List]

#### Project Highlights
- [Most interesting project]
- [Most challenging project]
- [Most educational project]

#### Learning Patterns
- Most productive times: [When you learn best]
- Most effective resources: [What helps most]
- Common obstacles: [What slows you down]

#### Goals for Next Month
1. [Goal 1 - Specific and measurable]
2. [Goal 2 - Specific and measurable]
3. [Goal 3 - Specific and measurable]

#### Long-term Vision
[How this month's learning contributes to your overall HPC goals]

---

## Tips for Using This Template

1. **Be Consistent**: Fill out the daily log every learning session
2. **Be Honest**: Record both successes and struggles
3. **Be Specific**: Include details that will help you later
4. **Review Regularly**: Look back at previous entries to see progress
5. **Adjust Goals**: Modify your goals based on what you learn about your learning style

## Example Entry

### Date: 2024-01-16

#### Today's Focus
- [x] Module: 01-fundamentals/02-mpi-hello-world
- [x] Concept: MPI point-to-point communication
- [x] Exercise: Modified hello_world.c to add message passing

#### Time Spent
- Start time: 14:00
- End time: 16:30
- Total time: 2 hours 30 minutes

#### What I Learned Today
- How MPI_Send and MPI_Recv work for point-to-point communication
- The importance of matching send and receive operations
- How to compile and run MPI programs with mpicc and mpirun

#### Code/Experiments
```c
// Added message passing between process 0 and process 1
if (rank == 0) {
    int message = 42;
    MPI_Send(&message, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    printf("Process 0 sent: %d\n", message);
} else if (rank == 1) {
    int received;
    MPI_Recv(&received, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    printf("Process 1 received: %d\n", received);
}
```

#### Output/Results
```
Hello from process 0 out of 4 on processor my-computer
Process 0 sent: 42
Hello from process 1 out of 4 on processor my-computer
Process 1 received: 42
Hello from process 2 out of 4 on processor my-computer
Hello from process 3 out of 4 on processor my-computer
```

#### Challenges Faced
- Initially forgot to match MPI datatypes in Send and Recv
- Had issues with tag matching between processes
- Output order was non-deterministic

#### Solutions Found
- Used MPI_INT consistently for both send and receive
- Used tag 0 for both operations
- Learned that MPI output order depends on process scheduling

#### Questions for Future Exploration
- How does MPI handle different data types?
- What happens if send and receive don't match?
- How can I ensure ordered output?

#### Mood/Reflection
- Feeling accomplished after getting message passing to work
- Frustrated by initial compilation errors but happy to solve them
- Excited to try collective operations next