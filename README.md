# Package Sorting System for Robotic Automation

## Overview
This repository contains a sorting algorithm designed for Thoughtful's robotic automation factory. The algorithm helps robotic arms dispatch packages to the correct stacks based on their physical properties.

## Sorting Criteria
Packages are sorted using the following criteria:

- **Bulky Package**: A package with volume (Width × Height × Length) ≥ 1,000,000 cm³ or any dimension ≥ 150 cm
- **Heavy Package**: A package with mass ≥ 20 kg

## Dispatch Categories
Packages are dispatched to one of these stacks:

- **STANDARD**: Normal packages (neither bulky nor heavy)
- **SPECIAL**: Packages that are either bulky or heavy, but not both
- **REJECTED**: Packages that are both bulky and heavy

## Implementation
The main function `sort(width, height, length, mass)` takes the dimensions (in centimeters) and mass (in kilograms) of a package and returns the appropriate stack designation.

## Usage
```python
# Example usage
result = sort(100, 50, 80, 15)  # Returns "STANDARD"
result = sort(160, 50, 80, 15)  # Returns "SPECIAL" (bulky due to width > 150cm)
result = sort(100, 50, 80, 25)  # Returns "SPECIAL" (heavy)
result = sort(160, 50, 80, 25)  # Returns "REJECTED" (both bulky and heavy)