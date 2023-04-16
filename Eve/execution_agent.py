from context_agent import ContextAgent
from babyagi import OpenAIConnector

class ExecutionAgent:
    def __init__(self,):
        self

    def run(self, objective: str, task: str) -> str:
        """
        Executes a task based on the given objective and previous context.
        Args:
            objective (str): The objective or goal for the AI to perform the task.
            task (str): The task to be executed by the AI.
        Returns:
            str: The response generated by the AI for the given task.
        """
    
        context = ContextAgent.run(query=objective, top_results_num=5)
        # print("\n*******RELEVANT CONTEXT******\n")
        # print(context)
        prompt = f"""
        You are an AI who performs one task based on the following objective: {objective}\n.
        Take into account these previously completed tasks: {context}\n.
        Your task: {task}\nResponse:"""
        return OpenAIConnector.openai_call(prompt, max_tokens=2000)