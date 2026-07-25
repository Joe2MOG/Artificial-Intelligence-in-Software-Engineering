# AI: Integrating Robust Error Handling in OOP

## Task Overview
This task applies AI-driven scaffolding to enhance a refactored Product class
by integrating robust exception handling and data validation using Python's
@property decorators and custom exceptions.

## Files
- `product_initial.py` — The original starting code with direct attribute
  assignment and no validation
- `product_refactored.py` — The enhanced version with @property setters,
  custom InvalidProductDataError exception, and test case for invalid input

## AI Tool Used
Gemini was used to scaffold the refactored solution. The prompt explicitly
requested @property decorator implementation, a custom exception class, and
a detailed explanation of data integrity and encapsulation design choices.

## Key Concepts
- **@property decorators** — Convert price and quantity into controlled
  attributes that route all assignments through validation logic
- **Custom exceptions** — InvalidProductDataError extends ValueError to
  provide meaningful, domain-specific error messages instead of generic crashes
- **Encapsulation** — Validation logic is hidden inside the Product class.
  External code interacts normally while protection runs silently underneath

## Test Result
When manager.inventory[0].quantity = -5 is executed, the program raises:
`InvalidProductDataError: Quantity cannot be negative. Received: -5`
The program does not crash. It catches and reports the error cleanly.
