from .specialized_agents import DataAnalyst, FinancialAdvisor, CustomerServiceRep

class Orchestrator:
    def __init__(self):
        self.agents = {
            'data_analyst': DataAnalyst(),
            'financial_advisor': FinancialAdvisor(),
            'customer_service': CustomerServiceRep()
        }

    def process_query(self, query):
        # For now, we'll just use the data analyst for all queries
        return self.agents['data_analyst'].process(query)
