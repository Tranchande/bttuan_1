def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Dưới chuẩn"
    elif 18.5 <= bmi < 25:
        return "Chuẩn"
    elif 25 <= bmi < 30:
        return "Thừa cân"
    elif 30 <= bmi < 40:
        return "Béo - nên giảm cân"
    else:
        return "Rất béo – cần giảm cân ngay"
weight_kg = float(input("Nhập cân nặng (kg): "))
height_m = float(input("Nhập chiều cao (m): "))
bmi = calculate_bmi(weight_kg, height_m)
status = interpret_bmi(bmi)
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
print(f"Tình trạng cân nặng: {status}")
