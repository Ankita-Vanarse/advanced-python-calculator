# Advanced Python Calculator

## Overview

This advanced Python calculator application serves as a demonstration of professional software development practices. It integrates various design patterns, a command-line interface (REPL), dynamic plugin support, comprehensive logging, and a robust calculation history management system utilizing Pandas.

## Features

- **Basic Operations**: Supports addition, subtraction, multiplication, and division.
- **Plugin System**: Allows for dynamic loading of plugins to extend functionality (e.g., power calculations).
- **Calculation History Management**: Uses Pandas to manage and persist calculation history.
- **Logging**: Detailed logging of operations, including error handling and operational insights.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create virtual environment**
   Ensure `virtualenv` package installed on system. If not, install it using  `pip install virtualenv`
   
   1. Run below command to create new environment for project
      ```
      virtualenv venv
      ```
   2. Activate environment:
      - Windows:
         ```
         venv\Scripts\activate
         ```
      - macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**:
   Ensure you have Python 3.6+ installed. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

5. **Environment Variables**:
   Set the necessary environment variables for logging and history management.

   Example:
   First create .env file in current folder.
   add below content to file
   ```py
   LOG_LEVEL = "INFO"
   HISTORY_FILE = "./data/history.csv"
   LOG_FILE = "./logs/log.log"
   ```

## Usage

### Running the Calculator

To start the calculator, execute the following command in your terminal:

```bash
python main.py
```

### Available Commands

Upon starting, the following commands will be available:

1. `add` - Add two or more numbers.
2. `subtract` - Subtract two numbers.
3. `multiply` - Multiply two or more numbers.
4. `divide` - Divide two numbers.
5. `load_history` - Load and display calculation history.
6. `clear_history` - Clear the calculation history.

### Example Command

To add two numbers:
```
>> add 5 10
Result: 15.0
```

To subtract two numbers:
```

>> subtract 25 15
Result: 10.0
```

To multiply three numbers:
```
>> multiply 2 4 5
Result: 40.0
```

To divide two numbers:
```
>> divide 40 10
Result: 4.0
```

To load history:
```
>> load_history
```

To clear history:
```
>> clear_history
```

## Design Patterns Used

- **Command Pattern**: Encapsulates the calculator commands for cleaner execution and management.
- **Facade Pattern**: Simplifies interactions with the history management system.
- **Factory Method**: Used for creating command instances dynamically.

## Logging

   - The application uses the built-in `logging` module to log operational messages, errors, and command results. 
   - The log level can be configured via environment variables.
   - Logs are stored in a specified file(data/log.log) for review.

## Plugins

The plugin system allows for easy extension of functionality. For example, the `PowerPlugin` can be used to calculate powers:

### Example Plugin Usage
To calculate the power of a number:
```
>> power 2 3
Plugin Result: 8
```

## Testing

The application uses `pytest` for unit testing. To run the tests, execute:

```bash
pytest
```


## Video Demonstration

A demonstration of the calculator's features and functionalities can be found [here](link-to-your-video).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- Thank you to the instructors and peers for feedback and support during this project.


man jogiya
heeriye slowed +reverb
tere dil ke shehar mai
jara jara
dhup lagdi
sath de tu mla
tere bin sanu sohneya



