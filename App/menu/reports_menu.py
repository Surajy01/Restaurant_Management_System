def reports():
    while True:
        print("\n╔═════════════════════════════════════╗")
        print("║      📊 REPORTS & ANALYTICS 📊      ║")
        print("╠═════════════════════════════════════╣")
        print("║ 1. 💰 Daily Sales Report            ║")
        print("║ 2. 📅 Monthly Sales Report          ║")
        print("║ 3. 🍽️  Top Selling Foods              ║")
        print("║ 4. 📈 Revenue Analysis              ║")
        print("║ 5. 🔙 Back                          ║")
        print("╚═════════════════════════════════════╝")

        choice=input("👉 Enter your choice: ")

        if choice=="1":
            print("Daily sales report")
            # daily_sales_report()

        elif choice=="2":
            print("Monthly sales report")
            # monthly_sales_report()

        elif choice=="3":
            print("Top sales report")
            # top_selling_foods()

        elif choice=="4":
            print("Revenue analysis")
            # revenue_analysis()

        elif choice=="5":
            print("🔙 Returning to Previous Dashboard")
            break

        else:
            print("❌ Invalid Choice!")
            