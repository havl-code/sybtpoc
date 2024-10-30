# SYBTPOC: Should You Buy This Piece of Clothing?

SYBTPOC is a simple, interactive Python program created for my AP Computer Science Principles (AP CSP) project. It helps users make thoughtful decisions about purchasing clothing by taking their input and promoting sustainable, conscious consumer habits.

## Features
- Guided Decision-Making: Users answer 10 questions about their item, such as its versatility, comfort, and quality.
- Score-Based Recommendation: The program provides an item grade based on the user's responses, helping to evaluate the item's long-term value.
- User-Friendly Table: A score table shows users clear, actionable advice.

## How it Works
1. Welcome Menu: Upon starting, the program displays a welcome message and options to learn about the program or begin evaluating an item.
2. Questionnaire: Users respond to 10 randomly selected questions with a “Yes” or “No” answer. Each “Yes” answer adds 10 points to the item grade.
3. Results & Recommendation: Based on the total score, the program advises if the item is a good investment.

| Score Range            | Recommendation                                               |
|------------------------|--------------------------------------------------------------|
| 0 < grade < 50         | Don’t buy it – save your money for a better item.            |
| 50 <= grade < 80       | Consider buying it but look for other options too.           |
| 80 < grade <= 100      | A great buy! You should definitely purchase this item.       |

## Principles Used
- Looping: Used to iterate over each question
- Selection: Applied to evaluate the responses and provide recommendations
- Sequencing: Ensures the program flows logically from input to output.

## Future Vision
SYBTPOC encourages users to shop consciously, contributing to a more sustainable future by promoting thoughtful spending habits.
