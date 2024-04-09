import NutritionPlanBuilder

class WeightGainNutrionPlanBuilder(NutritionPlanBuilder):
    def __init__(self):
        super().__init__()
        self.setFitnessGoal('weight loss')
