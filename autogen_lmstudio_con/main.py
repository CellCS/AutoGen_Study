from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

if __name__ == "__main__":
    # Load configuration list from JSON file
    config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
    
    # Configure Large Language Model (LLM)
    llm_config = {
        "request_timeout": 600,  # Set request timeout to 600 seconds
        "seed": 44,  # Set seed for reproducibility
        "config_list": config_list,  # Pass configuration list to LLM
        "temperature": 0  # Set temperature for model generation
    }

    # Initialize Assistant Agent
    agent_assistant = AssistantAgent(
        name="assistant",  # Name of the assistant agent
        llm_config={"config_list": config_list}  # Configuration for LLM
    )

    # Initialize User Proxy Agent
    user_proxy = UserProxyAgent(
        name="user_proxy",  # Name of the user proxy agent
        human_input_mode="ALWAYS",  # Set human input mode to always
        max_consecutive_auto_reply=10,  # Set maximum consecutive auto-reply
        code_execution_config={"work_dir": "coding", "use_docker": False}  # Code execution configuration
    )

    # Define tasks for evaluation
    tasks = [
        '''How do I determine if my study is an applicable clinical trial?''',
        '''Generate a 500-word essay on the impact of artificial intelligence on society. Measure the time taken to generate the response and the computational resources used.'''
    ]
    
    # Initiate chat between user proxy and assistant agent with one task
    user_proxy.initiate_chat(agent_assistant, message=tasks[0])
