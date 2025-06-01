import os
from qwen_agent.agents import Assistant
from qwen_agent.utils.output_beautify import typewriter_print
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

# Define LLM config
llm_cfg = {
    "model": "qwen/qwen3-32b:free",
    "model_server": "https://openrouter.ai/api/v1",
    "api_key": os.getenv('OPENROUTER_API_KEY'),
        "generate_cfg": {
        "max_tokens": 10000  # Specify the maximum number of output tokens
    }
}

# Define Tools
tools = [
    {'mcpServers': {  # You can specify the MCP configuration file
            'time': {
                'command': 'uvx',
                'args': ['mcp-server-time', '--local-timezone=Asia/Shanghai']
            },
            "fetch": {
                "command": "uvx",
                "args": ["mcp-server-fetch"]
            }
        }
    },
  'code_interpreter',  # Built-in tools
]

# Define Agent
bot = Assistant(llm=llm_cfg, function_list=tools)

# Streaming generation
response_plain_text = ''
messages = [{'role': 'user', 'content': 'what is the time now'}]
for responses in bot.run(messages=messages):
    response_plain_text = typewriter_print(responses, response_plain_text)

print(response_plain_text)