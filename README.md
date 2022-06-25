## Introduction
Repository made to simulate a simple redis operation. There are 2 base files:

1) redis_like.py with a class called Redis inside, with limited functionalities.
2) main.py, to generate a user interface via console to manage this Redis class


## How to execute locally
`cd {path_to_proejct}`

`python3 main.py`

### Commands formats
As asked by the stakeholders of this repository, the commands via console are limited to:

`GET <key>`

`SET <key><value>`

`UNSET <key>`

`NUMEQUALTO <value>`

`END`

`BEGGIN`

`COMMIT`

`ROLLBACK`

It's important to ensurue this format, with upper case on function and same whitespaces to work properly. Further upgrades can be done to turn into user friendly console.

### Examples
`SET <a1><123>`

`NUMEQUALTO <a1>`

`GET <a1>`

`END`

## Class functions

 - get(key)

 - set(key, value)

 - unset(key)

 - num_equal_to(key)

 - beggin

 - commit

 - rollback


## Tests considerations
#### Unit tests

Unit tests could be done using pytest tool, executing isolated Redis class functions with valid inputs to ensure the expected outputs.

#### Integration tests

Chain of calls could be done on differents Redis class functions to ensure data flow, could be used pytest also

#### Functional tests

A robot could be built to test the console interface main.py, testing invalid and valid inputs to ensure the file works properly. could be used PyUserInput to simulate those events, since needs a console handler. If was web app, Selenium webdrive could be used. I have a repository with this tool to create a robot to play a game, the repository is "aow_auto_clicker", go check it out! 