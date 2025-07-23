from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Waiting():
    """Waiting crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def richard(self) -> Agent:
        return Agent(
            config=self.agents_config['richard'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def equity_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['equity_analyst'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def forensic_accountant(self) -> Agent:
        return Agent(
            config=self.agents_config['forensic_accountant'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def industry_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['industry_specialist'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def regulatory_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['regulatory_analyst'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def corporate_lawyer_compliance_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['corporate_lawyer_compliance_expert'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def data_scientist_quant_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['data_scientist_quant_analyst'], # type: ignore[index]
            verbose=True
        )


    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def richard_persona(self) -> Task:
        return Task(
            config=self.tasks_config['richard_persona'], # type: ignore[index]
        )

    @task
    def research_company_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_company_task'], # type: ignore[index]
        )
    
    @task
    def financial_data_collection_task(self) -> Task:
        return Task(
            config=self.tasks_config['financial_data_collection_task'], # type: ignore[index]
        )
    
    @task
    def industry_competitive_analysis_collection_task(self) -> Task:
        return Task(
            config=self.tasks_config['industry_competitive_analysis_collection_task'], # type: ignore[index]
        )
    
    @task
    def management_governance_analysis_collection_task(self) -> Task:
        return Task(
            config=self.tasks_config['management_governance_analysis_collection_task'], # type: ignore[index]
        )
    
    @task
    def liquidity_risk_assessment_collection_task(self) -> Task:
        return Task(
            config=self.tasks_config['liquidity_risk_assessment_collection_task'], # type: ignore[index]
        )
    
    @task
    def define_investment_thesis_task(self) -> Task:
        return Task(
            config=self.tasks_config['define_investment_thesis_task'], # type: ignore[index]
        )
    
    @task
    def financial_due_diligence_task(self) -> Task:
        return Task(
            config=self.tasks_config['financial_due_diligence_task'], # type: ignore[index]
        )
    
    @task
    def industry_competitve_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['industry_competitve_analysis_task'], # type: ignore[index]
        )
    
    @task
    def management_governance_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['management_governance_analysis_task'], # type: ignore[index]
        )
    
    @task
    def risk_assesment_task(self) -> Task:
        return Task(
            config=self.tasks_config['risk_assesment_task'], # type: ignore[index]
        )
    
    @task
    def exit_strategy_liquidation_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['exit_strategy_liquidation_analysis_task'], # type: ignore[index]
        )
    
    @task
    def decision_task(self) -> Task:
        return Task(
            config=self.tasks_config['decision_task'], # type: ignore[index]
        )
    
    

    @crew
    def crew(self) -> Crew:
        """Creates the Waiting crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
