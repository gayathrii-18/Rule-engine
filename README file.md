# Rule Engine with AST

This project implements a simple 3-tier rule engine application using Abstract Syntax Trees (AST) to represent conditional rules.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix or MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python run.py`
6. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Create a rule by entering a rule name and rule string
2. Combine rules by entering rule names (one per line)
3. Evaluate a rule by entering the rule JSON and data JSON

## Testing

Run tests using: `python -m unittest discover tests`

## Security Considerations

- Input validation and sanitization should be implemented to prevent injection attacks
- Use HTTPS in production to encrypt data in transit
- Implement user authentication and authorization for multi-user scenarios
- Use parameterized queries to prevent SQL injection when working with databases

## Performance Optimization

- Implement caching for frequently accessed rules
- Use database indexing for faster rule retrieval
- Consider using a more efficient parsing algorithm for large and complex rules

## Future Improvements

- Implement a more robust error handling system
- Add support for more complex rule operations
- Develop a more user-friendly interface for rule creation and management
