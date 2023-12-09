Feature: Jugabilidad ahorcado

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
        Then Se muestra el modal de "Victoria"
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
        Then Se muestra el modal de "Victoria"
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
        Then Se muestra el modal de "Derrota"
        And El numero de intentos es "6"
        And La cantidad de vidas restantes es "0"
        
    Scenario: Verificar figura de ahorcado
        When Inicio nuevo juego
        Then La figura de ahorcado mostrada es "Soporte"
        When Ingreso la letra "A"
        Then La figura de ahorcado mostrada es "Soporte"
        When Ingreso la letra "C"
        Then La figura de ahorcado mostrada es "Cabeza"
        When Ingreso la letra "P"
        Then La figura de ahorcado mostrada es "Torso"
        When Ingreso la letra "E"
        Then La figura de ahorcado mostrada es "Brazo Izquierdo"
        When Ingreso la letra "F"
        Then La figura de ahorcado mostrada es "Brazo Derecho"
        When Ingreso la letra "G"
        Then La figura de ahorcado mostrada es "Pierna Izquierda"
        When Ingreso la letra "K"
        Then La figura de ahorcado mostrada es "Pierna Derecha"

