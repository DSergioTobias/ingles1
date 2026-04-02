# A simple program to convert temperatures from Celsius to Fahrenheit

def convert_to_fahrenheit(celsius):
    # Formula: F = (C × 9/5) + 32
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def classify_temperature(celsius):
    if celsius < 0:
        return "freezing"
    elif celsius < 20:
        return "cold"
    elif celsius < 30:
        return "warm"
    else:
        return "hot"

temperatures = [-5, 0, 18, 25, 37, 42]

for temp in temperatures:
    result = convert_to_fahrenheit(temp)
    label = classify_temperature(temp)
    print(f"{temp}°C → {result:.1f}°F — {label}")