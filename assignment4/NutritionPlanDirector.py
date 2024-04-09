class NutritionPlanDirector:
    def __init__(self, builder=None):
        self.builder = builder

    def setBuilder(self, builder):
        self.builder = builder

    def createNutritionPlan(self):
        if self.builder:
            return self.builder.build()
        else:
            return None
