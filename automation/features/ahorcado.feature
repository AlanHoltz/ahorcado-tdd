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
        And El numero de intentos es "4"
        And La cantidad de vidas restantes es "6"

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
        And El numero de intentos es "7"
        And La cantidad de vidas restantes es "3"

    Scenario: Perder juego
        When Inicio nuevo juego
        And Ingreso la letra "B"
        And Ingreso la letra "C"
        And Ingreso la letra "D"
        And Ingreso la letra "E"
        And Ingreso la letra "F"
        And Ingreso la letra "G"
        Then Se muestra pantalla de derrota
        And El numero de intentos es "6"
        And La cantidad de vidas restantes es "0"
        


