## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

Missing values or "NO DATA" entries in data/phase0.txt might be due to sensor problems, motion artifacts, power difficulties, or transmission errors. Filtering away these numbers results in clearer data, but it also involves risk. The removal of missing information may induce bias, making heart rate patterns look more steady than they are. It may also mask critical occurrences, such as unexpected heart rate decreases, which might indicate a health problem. Furthermore, disregarding these numbers without adequate management might skew statistical computations such as averages and variance. Instead of outright deletion, procedures like as interpolation or identifying missing data may give a more accurate and trustworthy analysis.

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

From our graphs, we can see that the phase the properly displays the heart rate during sleep is Phase0. This is because at Phase0, the maximum heart rate, from our calculations, can be seen as 93. With the graph, we see that after each 10 minute interval, the BPM goes down and stabilizes.

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings.

From our graphs, we can see that the phase the properly displays the heart rate during exercise is Phase2. This is because at Phase2, the maximum heart rate, from our calculations, can be seen as 117. With the graph, we see that after each 10 minute interval, the BPM goes constantly stays extremely high.

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

From our graphs, we can see that the phase the properly displays the average heart rate during regular periods of awake activity is Phase3. This is because at Phase3, the average heart rate, from our calculations, can be seen as 60.65. With the graph, we see that after each 10 minute interval, the BPM has a sharp spike and then goes down, causing the average to stabilize.
