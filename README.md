# Celsius Temperature Converter

## Description

This project is a command-line Python script that converts a predefined list of temperatures from Celsius to Fahrenheit. It is also a demonstration of core Python concepts including functions, conditional logic, iteration, and formatted output. The script processes six sample temperatures and produces a labeled result for each one.

## How it works

The program defines a function called convert_to_fahrenheit(celsius) that applies the standard conversion formula: (C × 9/5) + 32.
A second function, classify_temperature(celsius), evaluates a series of conditions and returns a descriptive label: "freezing", "cold", "warm", or "hot".
A list named temperatures holds six Celsius values: [-5, 0, 18, 25, 37, 42].
A for loop iterates over every item in the list and calls both functions for each temperature.
The script prints a formatted line to the console showing the Celsius value, the converted Fahrenheit result, and the classification label.
## Status

The project is currently running as a standalone script with no external dependencies. All features are complete and functional.
