import math
from datetime import datetime
import json

class BMICalculator:
    def __init__(self, weight, height, age, gender):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender.lower()
        
    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)
    
    def get_category(self):
        bmi = self.calculate_bmi()
        
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def get_ideal_weight_range(self):
        min_weight = 18.5 * (self.height ** 2)
        max_weight = 24.9 * (self.height ** 2)
        return round(min_weight, 2), round(max_weight, 2)
    
    def calculate_bmr(self):
        if self.gender == 'male':
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height * 100) - (5.677 * self.age)
        else:
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height * 100) - (4.330 * self.age)
        return round(bmr, 2)
    
    def get_calorie_needs(self, activity_level):
        bmr = self.calculate_bmr()
        activity_multipliers = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }
        
        multiplier = activity_multipliers.get(activity_level, 1.2)
        return round(bmr * multiplier, 2)

class HealthRecommendation:
    def __init__(self, bmi, category, age, gender):
        self.bmi = bmi
        self.category = category
        self.age = age
        self.gender = gender
        
    def get_health_risks(self):
        risks = []
        
        if self.category == "Underweight":
            risks = [
                "Weakened immune system",
                "Increased risk of malnutrition",
                "Osteoporosis and bone fractures",
                "Fertility issues",
                "Anemia and fatigue"
            ]
        elif self.category == "Overweight":
            risks = [
                "Type 2 diabetes risk",
                "High blood pressure",
                "Heart disease",
                "Joint problems",
                "Sleep apnea"
            ]
        elif self.category == "Obese":
            risks = [
                "Significantly increased risk of type 2 diabetes",
                "Cardiovascular diseases",
                "Certain types of cancer",
                "Stroke risk",
                "Liver disease",
                "Severe joint problems"
            ]
        else:
            risks = ["You are at a healthy weight with minimal risks"]
            
        return risks
    
    def generate_diet_plan(self):
        diet_recommendations = {
            'general_tips': [],
            'foods_to_include': [],
            'foods_to_avoid': [],
            'meal_structure': []
        }
        
        if self.category == "Underweight":
            diet_recommendations['general_tips'] = [
                "Increase calorie intake gradually",
                "Eat smaller, frequent meals (5-6 times daily)",
                "Focus on nutrient-dense foods",
                "Add healthy fats to meals"
            ]
            diet_recommendations['foods_to_include'] = [
                "Nuts and nut butters",
                "Whole grain bread and pasta",
                "Lean proteins (chicken, fish, eggs)",
                "Dairy products (milk, cheese, yogurt)",
                "Avocados and healthy oils",
                "Protein shakes and smoothies"
            ]
            diet_recommendations['foods_to_avoid'] = [
                "Empty calorie junk foods",
                "Excessive caffeine",
                "Foods that fill you up quickly without nutrition"
            ]
            
        elif self.category == "Normal weight":
            diet_recommendations['general_tips'] = [
                "Maintain current balanced eating habits",
                "Focus on whole, unprocessed foods",
                "Stay hydrated with 8-10 glasses of water daily",
                "Practice portion control"
            ]
            diet_recommendations['foods_to_include'] = [
                "Variety of colorful vegetables",
                "Fresh fruits",
                "Lean proteins",
                "Whole grains",
                "Healthy fats in moderation",
                "Low-fat dairy"
            ]
            diet_recommendations['foods_to_avoid'] = [
                "Excessive processed foods",
                "High sugar snacks and beverages",
                "Trans fats and excessive saturated fats"
            ]
            
        else:
            diet_recommendations['general_tips'] = [
                "Create a calorie deficit of 500-750 calories daily",
                "Eat protein with every meal to maintain muscle",
                "Fill half your plate with vegetables",
                "Track your food intake",
                "Drink water before meals"
            ]
            diet_recommendations['foods_to_include'] = [
                "Leafy green vegetables",
                "Lean proteins (chicken breast, fish, tofu)",
                "Legumes and beans",
                "Whole grains in controlled portions",
                "Berries and citrus fruits",
                "Green tea"
            ]
            diet_recommendations['foods_to_avoid'] = [
                "Sugary drinks and sodas",
                "Fried and deep-fried foods",
                "White bread and refined carbs",
                "Processed snacks and sweets",
                "High-calorie coffee drinks",
                "Excessive alcohol"
            ]
        
        diet_recommendations['meal_structure'] = self.get_meal_structure()
        return diet_recommendations
    
    def get_meal_structure(self):
        if self.category == "Underweight":
            return [
                "Breakfast: High-protein with healthy fats (eggs, avocado, whole grain toast)",
                "Mid-morning snack: Nuts and dried fruits",
                "Lunch: Balanced meal with protein, carbs, and vegetables",
                "Afternoon snack: Protein shake or yogurt with granola",
                "Dinner: Substantial meal with protein and complex carbs",
                "Before bed: Casein protein or milk with banana"
            ]
        elif self.category == "Normal weight":
            return [
                "Breakfast: Balanced with protein and fiber",
                "Mid-morning snack: Fruit or handful of nuts",
                "Lunch: Lean protein with vegetables and whole grains",
                "Afternoon snack: Greek yogurt or vegetables with hummus",
                "Dinner: Light meal with protein and vegetables"
            ]
        else:
            return [
                "Breakfast: High-protein, low-carb (egg whites, vegetables)",
                "Mid-morning snack: Small fruit or raw vegetables",
                "Lunch: Large salad with lean protein",
                "Afternoon snack: Protein shake or handful of almonds",
                "Dinner: Lean protein with steamed vegetables (no heavy carbs)"
            ]
    
    def generate_exercise_plan(self):
        exercise_plan = {
            'weekly_schedule': [],
            'cardio': [],
            'strength': [],
            'flexibility': []
        }
        
        if self.category == "Underweight":
            exercise_plan['weekly_schedule'] = [
                "Focus on strength training 3-4 times per week",
                "Minimal cardio (2 times per week, light intensity)",
                "Rest days are crucial for muscle growth"
            ]
            exercise_plan['strength'] = [
                "Compound exercises: Squats, deadlifts, bench press",
                "Progressive overload principle",
                "8-12 reps per set, 3-4 sets",
                "Focus on major muscle groups",
                "Rest 2-3 minutes between sets"
            ]
            exercise_plan['cardio'] = [
                "Light walking 20-30 minutes",
                "Avoid excessive cardio that burns too many calories"
            ]
            
        elif self.category == "Normal weight":
            exercise_plan['weekly_schedule'] = [
                "Mix of cardio and strength training",
                "150 minutes moderate cardio or 75 minutes vigorous per week",
                "Strength training 2-3 times per week",
                "Flexibility exercises daily"
            ]
            exercise_plan['cardio'] = [
                "Running, cycling, or swimming",
                "30-45 minutes per session",
                "Mix of steady-state and interval training"
            ]
            exercise_plan['strength'] = [
                "Full-body workout or split routine",
                "All major muscle groups",
                "8-15 reps per set"
            ]
            
        else:
            exercise_plan['weekly_schedule'] = [
                "Cardio 5-6 times per week",
                "Strength training 3 times per week",
                "Daily movement and activity",
                "Start slow and gradually increase intensity"
            ]
            exercise_plan['cardio'] = [
                "Brisk walking 45-60 minutes daily",
                "Swimming or cycling (low impact)",
                "Gradually progress to jogging",
                "High-Intensity Interval Training (HIIT) 2x per week",
                "Target heart rate: 60-70% of maximum"
            ]
            exercise_plan['strength'] = [
                "Full-body resistance training",
                "Focus on compound movements",
                "12-15 reps per set, 3 sets",
                "Bodyweight exercises initially",
                "Preserve muscle during weight loss"
            ]
        
        exercise_plan['flexibility'] = [
            "Daily stretching routine (10-15 minutes)",
            "Yoga or Pilates 1-2 times per week",
            "Mobility exercises for joints"
        ]
        
        return exercise_plan
    
    def generate_lifestyle_tips(self):
        tips = []
        
        if self.category == "Underweight":
            tips = [
                "Get 7-9 hours of quality sleep",
                "Manage stress through relaxation techniques",
                "Avoid skipping meals",
                "Consider consulting a nutritionist",
                "Monitor weight weekly and track progress",
                "Address underlying health issues with a doctor"
            ]
        elif self.category == "Normal weight":
            tips = [
                "Maintain current healthy habits",
                "Get regular health check-ups",
                "Stay active throughout the day",
                "Manage stress effectively",
                "Get adequate sleep (7-9 hours)",
                "Stay socially connected",
                "Practice mindful eating"
            ]
        else:
            tips = [
                "Set realistic weight loss goals (0.5-1 kg per week)",
                "Get 7-9 hours of sleep (poor sleep affects weight)",
                "Manage emotional eating triggers",
                "Find a support group or accountability partner",
                "Meal prep to avoid unhealthy choices",
                "Reduce screen time and increase movement",
                "Track progress with measurements, not just scale",
                "Consider consulting a healthcare provider"
            ]
            
        return tips

class BMIHealthSystem:
    def __init__(self):
        self.records = []
        
    def add_record(self, weight, height, age, gender, activity_level='moderate'):
        calculator = BMICalculator(weight, height, age, gender)
        bmi = calculator.calculate_bmi()
        category = calculator.get_category()
        min_weight, max_weight = calculator.get_ideal_weight_range()
        bmr = calculator.calculate_bmr()
        calories = calculator.get_calorie_needs(activity_level)
        
        health_rec = HealthRecommendation(bmi, category, age, gender)
        
        record = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'personal_info': {
                'weight': weight,
                'height': height,
                'age': age,
                'gender': gender,
                'activity_level': activity_level
            },
            'bmi_results': {
                'bmi': bmi,
                'category': category,
                'ideal_weight_range': f"{min_weight} - {max_weight} kg",
                'bmr': bmr,
                'daily_calorie_needs': calories
            },
            'health_assessment': {
                'risks': health_rec.get_health_risks(),
                'diet_plan': health_rec.generate_diet_plan(),
                'exercise_plan': health_rec.generate_exercise_plan(),
                'lifestyle_tips': health_rec.generate_lifestyle_tips()
            }
        }
        
        self.records.append(record)
        return record
    
    def display_results(self, record):
        print("\n" + "="*70)
        print("BMI CALCULATION RESULTS")
        print("="*70)
        
        info = record['personal_info']
        print(f"\nPersonal Information:")
        print(f"  Weight: {info['weight']} kg")
        print(f"  Height: {info['height']} m")
        print(f"  Age: {info['age']} years")
        print(f"  Gender: {info['gender'].title()}")
        print(f"  Activity Level: {info['activity_level'].replace('_', ' ').title()}")
        
        results = record['bmi_results']
        print(f"\n{'='*70}")
        print("BMI ANALYSIS")
        print("="*70)
        print(f"BMI: {results['bmi']}")
        print(f"Category: {results['category']}")
        print(f"Ideal Weight Range: {results['ideal_weight_range']}")
        print(f"Basal Metabolic Rate: {results['bmr']} calories/day")
        print(f"Daily Calorie Needs: {results['daily_calorie_needs']} calories/day")
        
        health = record['health_assessment']
        print(f"\n{'='*70}")
        print("HEALTH RISKS")
        print("="*70)
        for risk in health['risks']:
            print(f"  • {risk}")
        
        print(f"\n{'='*70}")
        print("PERSONALIZED DIET PLAN")
        print("="*70)
        diet = health['diet_plan']
        
        print("\nGeneral Diet Tips:")
        for tip in diet['general_tips']:
            print(f"  • {tip}")
        
        print("\nFoods to Include:")
        for food in diet['foods_to_include']:
            print(f"  • {food}")
        
        print("\nFoods to Avoid:")
        for food in diet['foods_to_avoid']:
            print(f"  • {food}")
        
        print("\nSuggested Meal Structure:")
        for meal in diet['meal_structure']:
            print(f"  • {meal}")
        
        print(f"\n{'='*70}")
        print("EXERCISE RECOMMENDATIONS")
        print("="*70)
        exercise = health['exercise_plan']
        
        print("\nWeekly Schedule:")
        for item in exercise['weekly_schedule']:
            print(f"  • {item}")
        
        if exercise['cardio']:
            print("\nCardiovascular Exercise:")
            for item in exercise['cardio']:
                print(f"  • {item}")
        
        if exercise['strength']:
            print("\nStrength Training:")
            for item in exercise['strength']:
                print(f"  • {item}")
        
        print("\nFlexibility & Mobility:")
        for item in exercise['flexibility']:
            print(f"  • {item}")
        
        print(f"\n{'='*70}")
        print("LIFESTYLE RECOMMENDATIONS")
        print("="*70)
        for tip in health['lifestyle_tips']:
            print(f"  • {tip}")
        
        print("="*70 + "\n")

def main():
    system = BMIHealthSystem()
    
    print("="*70)
    print("BMI CALCULATOR WITH HEALTH RECOMMENDATIONS")
    print("="*70)
    
    while True:
        print("\nEnter your details:")
        try:
            weight = float(input("Weight (kg): "))
            height = float(input("Height (meters, e.g., 1.75): "))
            age = int(input("Age (years): "))
            gender = input("Gender (male/female): ").lower()
            
            print("\nActivity Level:")
            print("  1. Sedentary (little or no exercise)")
            print("  2. Light (exercise 1-3 days/week)")
            print("  3. Moderate (exercise 3-5 days/week)")
            print("  4. Active (exercise 6-7 days/week)")
            print("  5. Very Active (intense exercise daily)")
            
            activity_choice = input("\nSelect activity level (1-5): ")
            activity_map = {
                '1': 'sedentary',
                '2': 'light',
                '3': 'moderate',
                '4': 'active',
                '5': 'very_active'
            }
            activity_level = activity_map.get(activity_choice, 'moderate')
            
            if weight <= 0 or height <= 0 or age <= 0:
                print("\nError: All values must be positive!")
                continue
            
            if gender not in ['male', 'female']:
                print("\nError: Gender must be 'male' or 'female'")
                continue
            
            record = system.add_record(weight, height, age, gender, activity_level)
            system.display_results(record)
            
            another = input("\nCalculate for another person? (yes/no): ").lower()
            if another not in ['yes', 'y']:
                break
                
        except ValueError:
            print("\nError: Please enter valid values!")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
    
    print("\nThank you for using BMI Calculator with Health Recommendations!")
    print("Stay healthy and take care! 💪")

if __name__ == "__main__":
    main()
