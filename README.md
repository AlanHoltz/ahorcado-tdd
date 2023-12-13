# Ahorcado TDD - Docs

[Ahorcado](http://34.176.37.34/)

## Instalar dependencias
```bash
pip install requirements.txt  
```

## Levantar Back-End
```bash
cd ahorcado-back
& d:/Repo/Agiles2023/ahorcado-tdd/venv/Scripts/Activate.ps1
py run.py           
```

## Levantar Front-End
```bash
cd ahorcado-front
npm install
npm start
```

- Navegar a [http://localhost:3000/](http://localhost:3000/)

## Correr tests unitarios
```bash
cd ahorcado-back
py ahorcado_unittests.py  
```


## Correr tests de aceptación

### Básico
```bash
behave automation/features         
```

### Con generación de reporte en Allure
#### Generar datos de reporte
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports automation/features
```
#### Levantar reporte
```bash
allure serve ./automation/reports
```


## Integraciones
- [Análisis estático de código - SonarCloud](https://sonarcloud.io/project/branches_list?id=ahorcado-tdd)
- [Code Coverage - CodeCov](https://app.codecov.io/gh/alexisjeriha/ahorcado-tdd)
- [Allure report - ATDD - (Implementación parcial)](https://alexisjeriha.github.io/ahorcado-tdd/27/)

