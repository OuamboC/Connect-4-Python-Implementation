## Object-Oriented Programming (OOP) in Connect 4 (Python)

### Introduction
This Connect 4 game implementation leverages Object-Oriented Programming (OOP) principles to create a modular, maintainable, and scalable codebase. By organizing the game into distinct classes, each responsible for specific aspects of the game logic, player interactions, 
and board management, we enhance code readability and facilitate easier updates and feature additions.

### Key Classes
1. **Player**:
   - **Responsibilities**: Manages player-specific data such as the player's name and token, and handles player actions.
   - **Attributes**: `name`, `token`.
   - **Methods**: `makeMove()`, which captures and returns the player's move.

2. **GameBoard**:
   - **Responsibilities**: Manages the game board's state, including initialization, move validation, token placement, and board display.
   - **Attributes**: `rows`, `cols`, `grid`.
   - **Methods**: `printGrid()`, `isValidMove()`, `placeToken()`, `getToken()`.

3. **GameLogic**:
   - **Responsibilities**: Handles the core game logic, including player switching, win condition checks, and the main game loop.
   - **Attributes**: `players`, `board`, `current_player_index`.
   - **Methods**: `switchPlayer()`, `checkWinner()`, `checkLine()`, `playGame()`.

### Justification for Using OOP
1. **Modularity**:
   - OOP allows the code to be broken down into self-contained modules (classes), each responsible for a specific aspect of the game. This modular approach makes it easier to understand, test, and maintain the code.
  
2. **Reusability**:
   - Classes and methods can be reused across different parts of the project or in future projects. For example, the `GameBoard` class can be reused or adapted for other grid-based games.

3. **Scalability**:
   - As the project grows, new features and enhancements can be added with minimal impact on existing code. The clear separation of responsibilities ensures that changes in one part of the code do not ripple unintended effects throughout the codebase.

4. **Ease of Maintenance**:
   - Bugs and issues can be isolated and resolved more quickly in an OOP structure. The use of classes makes it straightforward to track down where specific logic resides and modify it accordingly.

5. **Abstraction and Encapsulation**:
   - OOP encapsulates data and behavior within classes, providing a clear interface for interaction while hiding the internal workings. This abstraction simplifies the complexity of the system for users and developers alike.

### Conclusion
Using OOP in the Connect 4 game ensures a structured, efficient, and manageable codebase. The clear separation of concerns and the ability to easily extend and maintain the project make OOP an ideal choice for this implementation.
