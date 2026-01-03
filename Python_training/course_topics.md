# Python Core → ML/AI Foundation Roadmap

## 1. Python Fundamentals (DONE)
- Variables and data types
- Control flow (if / for / while / match)
- Functions and recursion
- Lambdas and comprehensions
- Built-in data structures (list, tuple, set, dict)
- Mutability vs immutability
- Truthiness and comparisons

## 2. Classes & Object-Oriented Design (DONE)
- Classes and instances
- State vs behavior
- __init__ and default values
- Instance vs class vs static methods
- Encapsulation (_ vs __, properties)
- __str__ vs __repr__
- Equality (__eq__) and identity
- Composition vs inheritance
- Polymorphism (duck typing, ABC basics)
- Inner classes (when and why)
- Dataclasses (mutable vs frozen)

## 3. File Handling & Persistence (DONE)
- Reading and writing files safely
- pathlib vs open()
- Append vs overwrite
- Defensive file handling
- JSON structure and rules
- Reading / writing JSON
- Input → validation → persistence
- Preventing duplicates
- Updating existing records

## 4. Modules & Program Structure (DONE)
- Splitting code into multiple files
- import vs from ... import
- Avoiding circular imports
- Module-level encapsulation
- if __name__ == "__main__"
- Designing clean module APIs
- Organizing small programs

## 5. Exceptions & Error Handling
- try / except / else / finally
- When to raise vs when to catch
- Custom exceptions
- Fail-fast vs silent failure
- Exception design for libraries
- Error handling with files and JSON

## 6. Testing & Debugging (Core Skill)
- Assertions and sanity checks
- Unit testing basics (unittest or pytest)
- Testing pure functions vs stateful code
- Debugging techniques
- Reading stack traces properly

## 7. Python Runtime & Internals (Light but Important)
- Namespaces and scope
- How imports actually work
- Object identity vs equality
- Reference semantics
- Garbage collection basics
- Performance intuition (not micro-optimizing)

## 8. Functional & Iteration Patterns
- Iterators and iterables
- Generators and yield
- next(), send(), close()
- map / filter / reduce (when NOT to use them)
- Lazy evaluation
- Memory-efficient patterns

## 9. Standard Library Mastery (Selective)
- pathlib
- json / csv
- datetime / time
- collections
- itertools
- functools
- typing (practical, not academic)

## 10. Environment & Tooling
- Virtual environments (venv)
- pip and dependency management
- requirements.txt
- Project layout conventions
- Running scripts vs packages

## 11. Data Handling Foundations (Before ML)
- Working with tabular data conceptually
- Data validation and cleaning
- Serialization vs deserialization
- Config-driven programs
- Reproducibility mindset

## 12. NumPy (Only After Foundations)
- Arrays vs Python lists
- Vectorized operations
- Broadcasting
- Memory model intuition
- When NumPy helps vs hurts

## 13. Pandas (Used Carefully)
- DataFrames as tools, not crutches
- Reading/writing data files
- Indexing pitfalls
- Avoiding silent bugs
- When NOT to use Pandas

## 14. Math & Statistics for ML
- Mean, median, variance
- Standard deviation
- Distributions
- Sampling intuition
- Numerical stability (conceptual)

## 15. Visualization (Optional but Useful)
- Matplotlib basics
- Reading plots critically
- Debugging data visually
- Avoiding misleading graphs

## 16. ML Libraries (Only Now)
- scikit-learn workflow
- Train/test split
- Overfitting intuition
- Metrics (confusion matrix, ROC, etc.)
- Model evaluation discipline

## 17. AI/ML Engineering Direction (Later)
- Pipelines
- Reproducibility
- Experiment tracking
- Deployment awareness
- Performance and reliability
