class ChatCompletionMessage:
    def __init__(self, content, role, function_call=None, tool_calls=None):
        self.content = content
        self.role = role
        self.function_call = function_call
        self.tool_calls = tool_calls or []

class Function:
    def __init__(self, arguments, name):
        self.arguments = arguments
        self.name = name

class ChatCompletionMessageToolCall:
    def __init__(self, id, function, type):
        self.id = id
        self.function = function
        self.type = type

def parse_messages(messages):
    system_message = ""
    tool_message = ""
    
    for message in messages:
        if isinstance(message, dict):  # 기존의 dict 타입 메시지 처리
            if message['role'] == 'system':
                system_message = message['content']
            elif message['role'] == 'tool':
                tool_message = message['content']
        elif isinstance(message, ChatCompletionMessage):  # ChatCompletionMessage 객체 처리
            if message.role == 'system':
                system_message = message.content
            elif message.role == 'tool' and message.tool_calls:
                for tool_call in message.tool_calls:
                    tool_message = tool_call.function.arguments
    
    return system_message, tool_message
