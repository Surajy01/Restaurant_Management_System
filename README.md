# 🍽️ Restaurant Management System 🍽️

A Python-based Restaurant Management System that helps manage food menus, customer orders, table reservations, billing, payments, staff management, and reports.

---

## 🚀 Features

### 👤 Authentication System
- User Registration (Admin, Staff, Customer)
- Secure Login
- Role-Based Access Control

### 👨‍💼 Admin Features
- Manage Food Menu
  - Add Food
  - Update Food
  - Delete Food
  - View Food Menu
- Manage Orders
  - View All Orders
  - Update Order Status
  - Cancel Orders
- Manage Staff
  - View All Staff
  - Staff Salary
- Manage Table Reservations
  - View All Bookings
  - Update Booking Status
- Reports & Analytics
  - Order Analytics Dashboard
  - Revenue Analysis
  - Monthly Sales Report

### 👨‍🍳 Staff Features
- View Menu
- Take Customer Orders
- Generate Bills
- Process Payments
- View Orders
- Update Order Status
- Manage Table Reservations

### 👤 Customer Features
- View Menu
- Place Orders
- View Order History
- Cancel Orders
- Table Reservation
- View My Bookings
- Cancel Booking
- Pay Bills

---

## 💳 Payment System

Supports multiple payment methods:

- Cash Payment
- Card Payment
- UPI Payment

Features:
- Payment Validation
- Payment Status Tracking
- Invoice Generation

---

## 🍽️ Food Management

Food Categories:

- Starters
- Breakfast
- Main Course
- Desserts
- Beverages

Food Information:
- Food Name
- Category
- Veg / Non-Veg
- Unit
- Stock
- Price

---

## 📅 Table Reservation System

Features:
- Reserve Table
- View Available Tables
- View My Bookings
- Cancel Booking
- Update Booking Status

Booking Status:
- Reserved
- Occupied
- Completed
- Cancelled

---

## 📦 Order Management

Order Status:
- Pending
- Preparing
- Ready
- Delivered
- Cancelled

Features:
- Place Order
- View Orders
- Update Status
- Cancel Orders
- Order History

---

## 📊 Reports & Analytics
- Monthly Sales Report
- Order Analysis
- Revenue Analysis


### Order Analytics Dashboard
- Total Orders
- Delivered Orders
- Pending Orders
- Cancelled Orders
- Delivery Percentage

### Revenue Analysis
- Total Revenue
- Paid Revenue
- Pending Revenue

### Monthly Sales Report
- Monthly Revenue
- Orders Count
- Sales Summary

---

## 📝 Logging System

Application logs are stored in:

```text
logs/
├── app.log
└── error.log
```

### app.log
Stores:
- User Login
- User Registration
- Order Placement
- Booking Creation
- Payment Success
- Food Management Activities

### error.log
Stores:
- Validation Errors
- Exceptions
- System Errors
- Payment Failures

---

## 🗂️ Project Structure

```text
Restaurant_Management_System/
│
├── app/
│   ├── auth/
│   │   ├── auth_service
│   ├── database/
│   │   ├── food.json
│   │   ├── sign_up.json
│   ├── domain/
│   │   ├── auth.py
│   │   ├── admin.py
│   │   ├── staff.py
│   │   ├── customer.py
│   │   ├── table.py
│   ├── food_management/
│   │   ├── add_food.py
│   │   ├── delete_food.py
│   │   ├── update_food.py
│   │   ├── view_food.py
│   ├── menu/
│   │   ├── auth_menu.py
│   │   ├── admin_menu.py
│   │   ├── staff_menu.py
│   │   ├── customer_menu.py
│   │   ├── table_menu.py
│   ├── order/
│   │   ├── order_place.py
│   ├── services/
│   │   ├── payment_services.py
│   │   ├── table_services.py
│   │   ├── revenue_analysis.py
│   │   ├── staff_salary.py
│   └── utils/
│       ├── file_handler.py
│       ├── logger.py
│
├── logs/
│   ├── app.log
│   └── error.log
│
├── main.py
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- JSON Database
- OOP Concepts
- File Handling
- Logging Module
- UUID
- Datetime
- Regular Expressions

---

## 🎯 OOP Concepts Implemented

- Classes & Objects
- Encapsulation
- Abstraction
- Inheritance (if applicable)
- Polymorphism (if applicable)
- Separation of Concerns

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to project folder

```bash
cd Restaurant_Management_System
```

3. Run the application

```bash
python main.py
```

---

## 👨‍💻 Author

**Suraj Yadav**

Python Developer Project:
Restaurant Management System

---

## 📄 License

This project is for learning and educational purposes.
