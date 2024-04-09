import NutritionPlanBuilder

class MaintenanceNutritionPlanBuilder(NutritionPlanBuilder):
    def __init__(self):
        super().__init__()
        self.setFitnessGoal('weight loss')