from app.food_management.view_food import ViewFoodManager
from app.food_management.add_food import AddFoodManager
from app.food_management.update_food import UpdateFoodManager
from app.food_management.dalate_food import DeleteFoodManager

def menu_management():
    while True:
        print("\n╔════════════════════════════════════════╗")
        print("║         🍽️  MENU MANAGEMENT 🍽️           ║")
        print("╠════════════════════════════════════════╣")
        print("║ 1. 📋 View Menu                        ║")
        print("║ 2. ➕ Add Food                         ║")
        print("║ 3. ✏️  Update Food                      ║")
        print("║ 4. ❌ Delete Food                      ║")
        print("║ 5. 🔙 Back                             ║")
        print("╚════════════════════════════════════════╝")

        choice=input("👉 Enter your choice: ")

        if choice=="1":
            ViewFoodManager().view_food_menu()

        elif choice=="2":
            AddFoodManager().add_food()

        elif choice=="3":
            UpdateFoodManager().update_food()

        elif choice=="4":
            DeleteFoodManager().delete_food()
            
        elif choice=="5":
            print("🔙 Returning to Previous Dashboard")
            break
        else:
            print("Invalid choice! Please try again.")