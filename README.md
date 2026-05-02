# 🏠 House Price Prediction

A Python command-line tool that estimates house prices in the Mumbai region using a weighted linear regression model. No external libraries needed — built from scratch.

## Features
- Predicts price based on area, bedrooms, location, and property age
- 5 location tiers with different scoring (Bandra to outskirts)
- Outputs estimated price + a realistic price range
- Displays results in Lakh / Crore format

## How to Run
1. Make sure Python is installed
2. Download `house_price_prediction.py`
3. Open terminal and run:
```bash
python house_price_prediction.py
```
4. Enter the property details when prompted

## Input Parameters
| Parameter      | Description                     |
|----------------|---------------------------------|
| Area           | Size of house in sq ft          |
| Bedrooms       | Number of bedrooms (BHK)        |
| Location       | Area tier in Mumbai (1–5)       |
| Property Age   | Age of property in years        |

## Tech Used
- **Language:** Python
- **Concepts:** Linear regression logic, weighted scoring, functions, input validation, data formatting

## Author
**Inamdar Mohammad Ali**  
B.E. Computer Science (AI & ML) — M.H. Saboo Siddiq College of Engineering, Mumbai
