# Engineering Team CrewAI Framework

A sophisticated multi-agent AI system that simulates a complete engineering team workflow, from system design to frontend implementation. This project demonstrates how AI agents can collaborate seamlessly to build real-world applications using the [CrewAI](https://crewai.com) framework.

## 🚀 Project Overview

The Engineering Team Crew consists of three specialized AI agents that work together to create complete software solutions:

- **Engineering Lead**: Creates comprehensive system designs and technical specifications
- **Backend Engineer**: Implements Python business logic with real code generation
- **Frontend Engineer**: Builds Gradio UIs that integrate with backend business logic

## 🏗️ Architecture

### Agents Configuration

#### 1. **Engineering Lead** (`engineering_lead`)
- **Role**: Python Engineering Lead
- **Experience**: 20+ years in system design and architecture
- **Responsibilities**: 
  - Create detailed system designs and technical specifications
  - Define use cases, user stories, and API contracts
  - Provide architectural patterns and implementation guidelines
  - Generate comprehensive documentation for team reference

#### 2. **Backend Engineer** (`backend_engineer`)
- **Role**: Python Backend Engineer  
- **Experience**: 10+ years in Python development
- **Responsibilities**:
  - Implement core business logic functions
  - Create Python methods for data processing and calculations
  - Generate sample data and test cases
  - Write executable code files that can be imported by other modules

#### 3. **Frontend Engineer** (`frontend_engineer`)
- **Role**: Python Frontend Engineer
- **Experience**: 8+ years in Python UI frameworks
- **Responsibilities**:
  - Build Gradio user interfaces
  - Integrate with backend business logic
  - Create interactive dashboards and data visualization
  - Ensure UI actually calls backend methods and displays real data

### Task Workflow

The crew follows a **sequential process** where each agent builds upon the previous work:

1. **System Design** → Engineering Lead creates comprehensive technical specifications
2. **Backend Implementation** → Backend Engineer implements business logic based on design
3. **Frontend Interface** → Frontend Engineer creates UI that connects to backend logic

## 🛠️ Features

### Core Capabilities

- **Real Code Generation**: Agents write actual executable Python files
- **Backend-Frontend Integration**: UI components import and use backend business logic
- **Docker Safety**: Code execution runs in secure Docker containers
- **Memory System**: Agents can learn from previous interactions
- **Error Handling**: Robust error handling and retry mechanisms

### Technical Stack

- **Framework**: CrewAI with Python 3.13
- **Backend**: Python with FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: Gradio for web interfaces
- **AI Models**: Google Gemini for agents, OpenAI for embeddings
- **Execution**: Docker for safe code execution
- **Memory**: RAG-based memory with SQLite storage

## 📁 Project Structure

```
engineering_team/
├── src/engineering_team/
│   ├── config/
│   │   ├── agents.yaml          # Agent configurations
│   │   └── tasks.yaml           # Task definitions
│   ├── crew.py                  # Crew orchestration
│   └── main.py                  # Entry point
├── output/                      # Generated files
│   └── habit-tracker-service/
│       └── AI Habit Progress Dashboard/
│           ├── system_design.md
│           ├── habit_progress.py
│           ├── app.py
│           └── sample_data.py
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python >=3.10 <3.14
- Docker (for safe code execution)
- API Keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`

### Installation

1. **Install UV package manager**:
```bash
pip install uv
```

2. **Install dependencies**:
```bash
crewai install
```

3. **Set up environment variables**:
```bash
# Create .env file with:
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
```

### Running the Crew

Execute the complete engineering workflow:

```bash
crewai run
```

This will:
1. Generate system design documentation
2. Create Python business logic files
3. Build Gradio UI that integrates with backend
4. Output all files to `./output/` directory

## 📋 Example Output

### System Design (`system_design.md`)
- Comprehensive technical specifications
- API contracts and data models
- Use cases and user stories
- Implementation guidelines

### Backend Logic (`habit_progress.py`)
```python
def calculate_completion_rate(progress_data):
    """Calculates habit completion rate"""
    # Real business logic implementation
    
def calculate_streak_length(progress_data):
    """Tracks current streak"""
    # Streak calculation logic
```

### Frontend Interface (`app.py`)
```python
import gradio as gr
from habit_progress import calculate_completion_rate, calculate_streak_length

def analyze_habit(habit_id, start_date, end_date):
    # UI function that calls backend methods
    completion_rate = calculate_completion_rate(progress_data)
    streak_length = calculate_streak_length(progress_data)
    return completion_rate, streak_length
```

## 🔧 Customization

### Adding New Agents

1. **Define agent in `config/agents.yaml`**:
```yaml
new_agent:
  role: "Your Agent Role"
  goal: "Agent's primary objective"
  backstory: "Agent's experience and expertise"
```

2. **Add agent method in `crew.py`**:
```python
@agent
def new_agent(self) -> Agent:
    return Agent(config=self.agents_config['new_agent'])
```

### Creating New Tasks

1. **Define task in `config/tasks.yaml`**:
```yaml
new_task:
  description: "Task description with {variables}"
  expected_output: "Expected deliverables"
  agent: "agent_name"
```

2. **Add task method in `crew.py`**:
```python
@task
def new_task(self) -> Task:
    return Task(config=self.tasks_config['new_task'])
```

## 🎯 Use Cases

This framework is perfect for:

- **Rapid Prototyping**: Generate complete applications from requirements
- **Code Generation**: Create working Python applications with UI
- **Team Simulation**: Model real engineering team workflows
- **Learning**: Understand full-stack development patterns
- **Automation**: Automate repetitive development tasks

## 🔍 Key Features Demonstrated

### 1. **Agent Collaboration**
- Sequential task execution with context passing
- Each agent builds upon previous work
- Shared memory and learning capabilities

### 2. **Real Code Generation**
- Agents write actual executable Python files
- No mock code - real business logic implementation
- Files can be imported and used by other modules

### 3. **Backend-Frontend Integration**
- Frontend actually imports backend modules
- UI calls real backend methods
- Displays calculated results, not hardcoded values

### 4. **Docker Safety**
- All code execution runs in secure containers
- Prevents system-level access
- Safe for production environments

## 🛡️ Security & Safety

- **Docker Isolation**: All code execution in containers
- **API Key Management**: Secure environment variable handling
- **Error Boundaries**: Robust error handling and recovery
- **Resource Limits**: Controlled execution time and memory usage

## 📚 Learning Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [Gradio Documentation](https://gradio.app/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Docker Documentation](https://docs.docker.com)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

- **Documentation**: [CrewAI Docs](https://docs.crewai.com)
- **Community**: [Discord](https://discord.com/invite/X4JWnZnxPb)
- **GitHub**: [CrewAI Repository](https://github.com/joaomdmoura/crewai)
- **Issues**: Report bugs and request features

---

**Built with ❤️ using CrewAI Framework**

*Empowering AI agents to collaborate and build amazing software together.*
