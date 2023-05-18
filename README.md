## OVERVIEW
- You have been hired as a developer for a new project where,
- You will write a Django app to track corporate assets such as phones, tablets, laptops and other gears handed out to employees.

## GOALS
- The application might be used by several companies
- Each company might add all or some of its employees
- Each company and its staff might delegate one or more devices to employees for a certain period of time
- Each company should be able to see when a Device was checked out and returned
- Each device should have a log of what condition it was handed out and returned

## DESIGN
A class rough diagram of the implementation:

![Class Diagram](./images/class_diagram.jpg)

## USAGE
1. create venv inside root folder
2. activate source
3. makemigrations and migrate
4. runserver

## APIs and URLs
### _Root URL_
- root: http://127.0.0.1:8000/api/

### _Company URLs_
- Register a new company account: http://127.0.0.1:8000/api/register
    - POST Format
        ```
        { "company_name" : "abc", "password": "pass"}
        ```

- Login using registered account: http://127.0.0.1:8000/api/login
    - POST Format
        ```
        { "company_name" : "abc", "password": "pass"}
        ```

- Logout: http://127.0.0.1:8000/api/logout

### _Device URLs_
- Add new Devices to logged in company: http://127.0.0.1:8000/api/devices/add
    - POST Format
        ```
        [
            { "device_name": "iphone 11 pro max - 786", "status" : "used" },
            { "device_name": "iphone 12 pro max - 921", "status" : "broken" },
            { "device_name": "iphone 13 pro max - 101", "status" : "new" },
            { "device_name": "iphone 14 pro max - 211", "status" : "new" },
            { "device_name": "iphone 15 pro max - 311", "status" : "new" }
        ]
        ```

- List all devices of logged in company: http://127.0.0.1:8000/api/devices/list

### _Employee URLs_
- Add new Employees to logged in company: http://127.0.0.1:8000/api/employees/add
    - POST Format
        ```
        [
            { "employee_name" : "saif"},
            { "employee_name" : "ridy"},
            { "employee_name" : "purba"},
            { "employee_name" : "nishat"},
            { "employee_name" : "blu"}
        ]        
        ```

- List all Employees of logged in company: http://127.0.0.1:8000/api/employees/list


### _DeviceLog URLs_   
- Delegate devices to employees to employees of logged in company: http://127.0.0.1:8000/api/devices/delegate

    - POST Format (Assumption: Front-end will display list of selectable valid Devices and Employees)
        ```
        [
            { "device_name": "iphone 11 pro max - 786", "employee_name" : "blu" },
            { "device_name": "iphone 12 pro max - 921", "employee_name" : "blu" },
            { "device_name": "iphone 13 pro max - 101", "employee_name" : "saif" },
            { "device_name": "iphone 14 pro max - 211", "employee_name" : "saif" },
            { "device_name": "iphone 15 pro max - 311", "employee_name" : "purba" }
        ]        
        ```

- Return a device delegated to an employee: http://127.0.0.1:8000/api/devices/return

    - POST Format (Assumption: Returns are made one by one)
        ```
        {
            "device_name": "iphone 11 pro max - 786",
            "employee_name": "blu",
            "return_condition": "broken"
        }        
        ```

- List all delegations of company devices: http://127.0.0.1:8000/api/devices/delegations