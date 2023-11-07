Feature: Ahorcado

    Scenario: My Scenario
        Given I open ahorcado page
        When ingreso la letra "a"
        Then el juego me muestra "a"
    
    Scenario: My Scenario fail
        Given I open ahorcado page
        When ingreso la letra "b"
        Then el juego no muestra "b"