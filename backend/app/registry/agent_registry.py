import os
import importlib
import inspect
from typing import Dict, List, Type
from rich.console import Console
from app.agents.base import BaseAgent

console = Console()

class AgentRegistry:
    def __init__(self):
        self._agents: Dict[str, BaseAgent] = {}
        self._categories: Dict[str, List[BaseAgent]] = {}

    def register(self, agent_class: Type[BaseAgent]):
        agent_instance = agent_class()
        self._agents[agent_instance.name] = agent_instance
        
        if agent_instance.category not in self._categories:
            self._categories[agent_instance.category] = []
        self._categories[agent_instance.category].append(agent_instance)

    def get_agent(self, name: str) -> BaseAgent | None:
        return self._agents.get(name)

    def get_category(self, category_name: str) -> List[BaseAgent]:
        return self._categories.get(category_name, [])

    def get_all(self) -> List[BaseAgent]:
        return list(self._agents.values())

    def get_all_categories(self) -> List[str]:
        return list(self._categories.keys())

    def search(self, query: str) -> List[BaseAgent]:
        query = query.lower()
        return [
            agent for agent in self._agents.values()
            if query in agent.name.lower() or query in agent.description.lower() or query in agent.category.lower()
        ]

    def autodiscover(self):
        """
        Dynamically imports all modules in the agents directory and registers subclasses of BaseAgent.
        """
        agents_dir = os.path.join(os.path.dirname(__file__), '..', 'agents', 'categories')
        
        if not os.path.exists(agents_dir):
            console.print(f"[bold red]Agents directory not found at {agents_dir}[/bold red]")
            return

        for root, _, files in os.walk(agents_dir):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    # Convert file path to module path
                    rel_dir = os.path.relpath(root, os.path.join(os.path.dirname(__file__), '..', '..'))
                    module_path = rel_dir.replace(os.sep, '.') + '.' + file[:-3]
                    
                    try:
                        module = importlib.import_module(module_path)
                        for name, obj in inspect.getmembers(module):
                            if inspect.isclass(obj) and issubclass(obj, BaseAgent) and obj is not BaseAgent:
                                self.register(obj)
                    except Exception as e:
                        console.print(f"[bold red]Failed to load module {module_path}: {e}[/bold red]")
        
        console.print(f"[bold green]Registered {len(self._agents)} agents across {len(self._categories)} categories.[/bold green]")

registry = AgentRegistry()
