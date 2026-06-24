from app.order.order_analytics import OrderAnalyticsService
from app.services.revenue_analysis import RevenueAnalysisService
from app.services.monthly_sales import MonthlySalesReportService


def reports():
    while True:
        print("\n╔═════════════════════════════════════╗")
        print("║      📊 REPORTS & ANALYTICS 📊      ║")
        print("╠═════════════════════════════════════╣")
        print("║ 1. 💰 Daily Sales Report(N/A)       ║")
        print("║ 2. 📅 Monthly Sales Report          ║")
        print("║ 3. 🍽️  Top Selling Foods(N/A)        ║")
        print("║ 4. 📊 Order Analysis                ║")
        print("║ 5. 📈 Revenue Analysis              ║")
        print("║ 6. 🔙 Back                          ║")
        print("╚═════════════════════════════════════╝")

        choice=input("👉 Enter your choice: ")

        if choice=="1":
            print("Daily sales report")
            # daily_sales_report()

        elif choice=="2":
            MonthlySalesReportService("app/database/orders.json").show_monthly_sales_report()
            # print("Monthly sales report")

        elif choice=="3":
            print("Top sales report")
            # top_selling_foods()

        elif choice=="4":
            OrderAnalyticsService("app/database/orders.json").show_orderanalytics_dashboard()
            # print("Order analysis")

        elif choice=="5":
            RevenueAnalysisService("app/database/orders.json").show_revenue_dashboard()
            # print("Revenue analysis")

        elif choice=="6":
            print("🔙 Returning to Previous Dashboard")
            break

        else:
            print("❌ Invalid Choice!")
            
            