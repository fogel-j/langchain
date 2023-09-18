# flake8: noqa
PREFIX = f"""Answer the following questions as best you can. 
For context, the current day is {{current_date}}
You can only perform a MAXIMUM of 3 actions.
You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do, however be very concise
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can only occur for a MAXIMUM of 3 times, so plan the API calls accordingly)
Thought: I now know the final answer
Final Answer: the final answer to the original input question"""
SUFFIX = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""
