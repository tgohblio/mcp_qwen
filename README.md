# MCP Qwen Project

## Installation

Follow the steps below to set up the MCP Qwen project:

### Prerequisites
- Python 3.11 or higher
- `pip` package manager
- Access to OpenRouter API (API key required)
- `uv` command-line tool installed

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/mcp_qwen.git
   cd mcp_qwen
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   Run the following command to install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install `uv`**:
   Install the `uv` command-line tool, which is required for MCP server commands:
   ```bash
   brew install uv
   ```

5. **Configure Environment Variables**:
   Create a `.env` file in the project root and add your OpenRouter API key:
   ```env
   OPENROUTER_API_KEY=your_api_key_here
   ```

   To obtain the API key:
   - Visit [OpenRouter](https://openrouter.ai/) and sign up for an account.
   - Generate an API key from your account dashboard.

## Run

To execute the project, run the following command:
```bash
python main.py
```

This will start the application and process the defined tasks using the Qwen agent.