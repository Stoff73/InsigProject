# Waiting Crew

I have made a number of changes, the agents, currently, do not have internet access, ecept for research, in order to fetch data. To change this we can modify to search a database, vectorstore or anything else really.

I do still need to put in correct structured output classes, I have just used the agent 'expected output' property for this, not the best solution as can be janky.

I have kept memory off, except for the main agent, as well as assignments for now.

Tested the logic, seems to work, the prompts seems to be okay, although a bit big. Turning verbose off helps with this, I am of course useing 4.1-mini, so using a bigger model will help, but cost more.

Welcome to the Waiting Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/waiting/config/agents.yaml` to define your agents
- Modify `src/waiting/config/tasks.yaml` to define your tasks
- Modify `src/waiting/crew.py` to add your own logic, tools and specific args
- Modify `src/waiting/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the waiting Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Understanding Your Crew

The waiting Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Waiting Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
