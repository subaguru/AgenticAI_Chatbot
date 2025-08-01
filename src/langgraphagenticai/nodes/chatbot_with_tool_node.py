from src.langgraphagenticai.state.state import State

class ChatbotwithToolNode:
    """
    Chatbot logic enhanced with tool integration.
    """
    def __init__(self,model):
        self.llm = model

    def process(self, state:State)->dict:
        """
        Processes the input state and generates a response with tool integration.
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role":"user", "content":user_input}])

        #Simulate Tool specific logic
        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]}
    
    def createchatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state:State):
            """
            Chatbot logic for processing the input state and returning a response
            """

            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node