class NutritionPlan:
    def __init__(self, daily_caloric_intake=0, macronutrient_ratios=None, meal_plans=None, fitness_goal='', dietary_restrictions=None):
        self.daily_caloric_intake = daily_caloric_intake
        self.macronutrient_ratios = macronutrient_ratios if macronutrient_ratios is not None else {'carbohydrates': 0, 'proteins': 0, 'fats': 0}
        self.meal_plans = meal_plans if meal_plans is not None else []
        self.fitness_goal = fitness_goal
        self.dietary_restrictions = dietary_restrictions if dietary_restrictions is not None else []

    def __str__(self):
        return (f"Fitness Goal: {self.fitness_goal}\n"
                f"Dietary Restrictions: {', '.join(self.dietary_restrictions)}\n"
                f"Daily Caloric Intake: {self.daily_caloric_intake} calories\n"
                f"Macronutrient Ratios: {self.macronutrient_ratios}\n"
                f"Meal Plans: {self.meal_plans}")
