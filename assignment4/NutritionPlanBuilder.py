import NutritionPlan

class NutritionPlanBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.nutrition_plan = NutritionPlan()

    def setCaloricIntake(self, calories):
        self.nutrition_plan.daily_caloric_intake = calories
        return self

    def setMacronutrientRatios(self, carbohydrates, proteins, fats):
        self.nutrition_plan.macronutrient_ratios = {'carbohydrates': carbohydrates, 'proteins': proteins, 'fats': fats}
        return self

    def setMealPlans(self, meal_plans):
        self.nutrition_plan.meal_plans = meal_plans
        return self

    def setFitnessGoal(self, goal):
        self.nutrition_plan.fitness_goal = goal
        return self

    def setDietaryRestrictions(self, restrictions):
        self.nutrition_plan.dietary_restrictions = restrictions
        return self

    def build(self):
        built_nutrition_plan = self.nutrition_plan
        self.reset()
        return built_nutrition_plan
