Feature: Ahorcado

    Scenario: Salir del juego
        When Inicio nuevo juego
        And Salgo del juego
        Then Estoy en la página inicial

    Scenario: Ganar juego sin fallos
        When Inicio nuevo juego
        And Ingreso la letra "H"
        And Ingreso la letra "O"
        And Ingreso la letra "L"
        And Ingreso la letra "A"
        Then Se muestra pantalla de victoria
        Then El numero de intentos es "4"
        Then La cantidad de vidas restantes es "6"

    Scenario: Ganar juego con fallos
        When Inicio nuevo juego
        And Ingreso la letra "H"
        And Ingreso la letra "B"
        And Ingreso la letra "O"
        And Ingreso la letra "L"
        And Ingreso la letra "R"
        And Ingreso la letra "N"
        And Ingreso la letra "A"
        Then Se muestra pantalla de victoria
        Then El numero de intentos es "7"
        Then La cantidad de vidas restantes es "3"

    Scenario: Perder juego
        When Inicio nuevo juego
        And Ingreso la letra "B"
        And Ingreso la letra "C"
        And Ingreso la letra "D"
        And Ingreso la letra "E"
        And Ingreso la letra "F"
        And Ingreso la letra "G"
        And Ingreso la letra "H"
        And Ingreso la letra "I"
        And Ingreso la letra "J"
        And Ingreso la letra "K"
        And Ingreso la letra "M"
        And Ingreso la letra "P"
        Then Se muestra pantalla de derrota
        Then El numero de intentos es "6"
        Then La cantidad de vidas restantes es "0"
        


