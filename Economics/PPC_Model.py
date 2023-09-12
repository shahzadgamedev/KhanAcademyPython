# Production Possibility Curve Model

# A Class To Represent The PPC Scenario
class PPC_Scenario:
    def __init__(self, name, resources, products):
        self.name = name
        self.resources = resources
        self.products = products

    def __str__(self):
        scenario_definition = "Scenario: " + self.name + "\n"
        resource_definition = "Resources: " + str(self.resources) + "\n"
        product_definition = "Products: " + str(self.products) + "\n"
        return scenario_definition + resource_definition + product_definition

    def __repr__(self):
        return self.name

    def GetOpportunityCost(self, OtherScenario):
        """
        Calculate the Opportunity Cost of Moving from this Scenario to another
        :type OtherScenario: PPC_Scenario

        :return: The Opportunity Cost of Moving from this Scenario to another
        """
        if OtherScenario.name == self.name:
            return "Same Scenario"

        elif OtherScenario.resources >= self.resources and OtherScenario.products >= self.products:
            return "Infinite"
        return 0
