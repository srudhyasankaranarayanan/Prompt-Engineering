def build_prompt(technique, task):
    
    if technique == "Few-shot":
        return f"""
You are given several examples. Observe the pattern and answer
the new task in a similar way.

Example 1:
Question: What is HTML?
Answer: HTML is a markup language used to structure content
on web pages.

Example 2:
Question: What is CSS?
Answer: CSS is used to style and design the appearance of
web pages.

Example 3:
Question: What is JavaScript?
Answer: JavaScript is a programming language used to add
dynamic and interactive behavior to web pages.

New Task:
{task}

Give an answer following the style of the examples.
""".strip()

    if technique == "Zero-shot":
        return f"""
Answer the following task directly using your existing knowledge.

Task:
{task}

Give a clear, accurate, and relevant answer.
""".strip()

    if technique == "ToT":
        return f"""
Explore different possible approaches before selecting the
most suitable solution.

Approach 1:
Consider the first possible solution.

Approach 2:
Consider another possible solution.

Approach 3:
Consider an alternative solution if useful.

Selection:
Compare the approaches and select the most appropriate one.

Task:
{task}

Provide the selected solution with a brief explanation.
Do not reveal private or hidden chain-of-thought.
""".strip()

    if technique == "One-shot":
        return f"""
Use the following example as a guide for answering the task.

Example:
Question: What is React?
Answer: React is a JavaScript library used to build reusable
and interactive user interfaces, especially for web applications.

Now answer this task in a similar style:

Question:
{task}
""".strip()

    if technique == "Manual CoT":
        return f"""
Solve the task using the following structured process.

Step 1 - Understand:
Identify what the task is asking.

Step 2 - Analyze:
Identify the important information.

Step 3 - Apply:
Use the appropriate concept or method.

Step 4 - Verify:
Check whether the result is reasonable.

Step 5 - Answer:
Give the final answer clearly.

Task:
{task}

Do not reveal private or hidden chain-of-thought.
""".strip()

    if technique == "CoT":
        return f"""
Solve the task systematically.

First understand the problem.
Then identify the important information.
Next apply the appropriate reasoning or method.
Finally provide the answer with a short explanation of the
important steps.

Task:
{task}

Do not reveal private or hidden chain-of-thought.
""".strip()

    if technique == "React":
        return f"""
Solve the task using a ReAct-style approach.

Thought:
Briefly identify what needs to be determined.

Action:
Identify what action, calculation, or operation would help.

Observation:
Consider the result or information obtained from that action.

Final:
Provide the final answer based on the available information.

Task:
{task}

Do not reveal private or hidden chain-of-thought.
Only provide a concise explanation and final answer.
""".strip()

    if technique == "Direct Stimulus Prompting":
        return f"""
You are given a direct stimulus related to the task.

Stimulus:
The user wants a practical and easy-to-understand answer.
The response should focus only on information relevant to the
given task.

Task:
{task}

Respond directly to the stimulus.
Avoid unnecessary background information and provide the most
useful answer first.
""".strip()

    if technique == "Self-consistency":
        return f"""
Solve the following task using multiple possible reasoning
paths.

Path 1:
Find a possible solution.

Path 2:
Solve the task using another approach.

Path 3:
Try a different approach if applicable.

Consistency Check:
Compare the results from the different approaches.
Identify the answer that is most consistently supported.

Task:
{task}

Provide the final answer and a short justification.
Do not reveal private or hidden chain-of-thought.
""".strip()

    if technique == "Role based":
        return f"""
You are an experienced software development mentor.

Your responsibilities are:
- Explain technical concepts clearly.
- Use simple terminology.
- Give practical examples when useful.
- Focus on helping a beginner understand the topic.

Task:
{task}

Answer the task from the perspective of a software development
mentor.
""".strip()

    if technique == "Instruction tuning":
        return f"""
Follow these instructions carefully.

Instructions:
1. Understand the user's task.
2. Answer only what is requested.
3. Use simple and precise language.
4. Organize the response logically.
5. Include examples when they improve understanding.
6. Avoid irrelevant information.
7. Make the final response easy to read.

Task:
{task}

Generate the answer by following all the instructions above.
""".strip()

    else:
        raise ValueError(
            f"Unsupported prompting technique: {technique}"
        )