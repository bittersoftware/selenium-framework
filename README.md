# selenium-framework
Selenium framework with python

# Install dependencies
Create and activate a virtual environment:  
```python3 -m venv venv```  
```source venv/bin/activate```  

Install requirements:  
```pip3 install -r requirements.txt```  

# Execute tests
Select browser with environment variable:  
```export BROWSER=Chrome```  

Run all tests with logs:  
```pytest -s --log-cli-level=INFO```

Run specific test by pytest.mark:  
```pytest -m tcid1 -s --log-cli-level=INFO```

# Structure
```
.
├── conftest.py
├── __init__.py
├── pytest.ini
├── src
│   ├── configs
│   ├── helpers
│   │   ├── config_helpers.py
│   │   ├── generic_helpers.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── pages
│   │   ├── GenericItems.py
│   │   ├── GetStartedPage.py
│   │   ├── HomePage.py
│   │   ├── __init__.py
│   │   ├── locators
│   │   ├── OrderProcess.py
│   │   ├── SharedHosting.py
│   │   └── WordPressHosting.py
│   └── SeleniumExtended.py
└── tests
    ├── add_to_chart
    │   ├── __init__.py
    │   └── test_add_to_chart.py
    ├── get_started
    │   ├── __init__.py
    │   ├── test_1year_products.py
    │   ├── test_2year_products.py
    │   └── test_get_started.py
    ├── home
    │   ├── __init__.py
    │   ├── test_open_compare_plans.py
    │   └── test_open_nav_menu.py
    └── __init__.py
```