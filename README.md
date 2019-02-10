[![Maintainability](https://api.codeclimate.com/v1/badges/494a680484727eb34440/maintainability)](https://codeclimate.com/github/kimpetertanui/Politico/maintainability)

[![Build Status](https://travis-ci.org/kimpetertanui/Politico.png?branch=develop)](https://travis-ci.org/kimpetertanui/Politico)

[![Coverage Status](https://coveralls.io/repos/github/kimpetertanui/Politico/badge.png?branch=develop)](https://coveralls.io/github/kimpetertanui/Politico?branch=develop)




- - - -

# POLITICO API #


## Summary ##

    Politico API is a backend platform that implements the voting process.
    Politicians can run for different political offices and be voted in by the users.
    The admin can create political parties and offices.This platform enables citizens give their mandate
    to politicians running for different government offices while building trust in the process through transparency.
    This plartform is managed by pivotal tracker board. Click<a href="https://www.pivotaltracker.com/n/projects/2241686">here</a>to view it.

    The site is hosted on heroku

## Getting Started ##

  1.Clone the repository by doing: git clone  https://github.com/kimpetertanui/Politico.git

  2.Create a virtual environment: virtualenv env

  3.Activate the virtual environment: source venv/bin/activate on Linux/Mac or source venv/Scripts/activate on windows.

  4.Install the requirements : pip install -r requirements.txt

## How to run tests ##
   Use pytest to run: pytest --cov=app

## Pre-requisites ##
    1.Postman
    2.Git
    3.Python3

 ## Running it on machine##
    Clone this repository to your computer:
    git clone: https://github.com/kimpetertanui/Politico.git

    cd into this folder:
    Politico-api

    Create a virtual environment
    python3 -m venv env

    Activate the virtual environment
    source venv/bin/activate

    Switch to 'develop' branch
    git checkout develop

    Install requirements
    pip3 install -r requirements.txt

    Run app
    python3 run.py

    Run tests
    pytest


### This List below shows the endpoints that enable one to: ###

    1.Create account and log in
    2.Create a political party
    3.Fetch a specific political party
    4.Fetch all political parties
    5.Edit a specific political party
    6.Delete a specific political party
    7.Create a political office
    8.Fetch all political offices
    9.Create candidate for a specific office election
    10.Vote for a candidate for a specific office election

## Use Postman to test following working Endpoinsts  ##

            ENDPOINT  | FUNCTIONALITY
        ------------- | -------------
        POST /api/v1/parties  | CREATE political party
        GET political parties  | GET ALL political parties
        GET /api/v1/parties/int:partyID| GET ONE political party
        DELETE /api/v1/parties|DELETE ONE political party
        PATCH /api/v1/parties/int:partyID|UPDATE ONE political party
        POST /api/v1/offices|CREATE government office
        GET /api/v1/offices/int:officeID|GET ONE government office
        GET /api/v1/offices|GET ALL government offices


## Endpoints ##
   ENDPOINT  |    ENDPOINT
------------- | -------------
POST /api/v1/parties   | CREATE political party
GET political parties  | GET ALL political parties
GET /api/v1/parties/int:partyID | GET ONE political party
DELETE /api/v1/parties | DELETE ONE political party
PATCH /api/v1/parties/int:partyID|UPDATE ONE political party
POST /api/v1/offices  | CREATE government office
GET /api/v1/offices/int:officeID | GET ONE government office
GET /api/v1/offices | GET ALL government offices
 
```
    ENDPOINT  |    ENDPOINT
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
```

`code()`

    Markup :  `code()`

```javascript
    var specificLanguage_code =
    {
        "data": {
            "lookedUpPlatform": 1,
            "query": "Kasabian+Test+Transmission",
            "lookedUpItem": {
                "name": "Test Transmission",
                "artist": "Kasabian",
                "album": "Kasabian",
                "picture": null,
                "link": "http://open.spotify.com/track/5jhJur5n4fasblLSCOcrTp"
            }
        }
    }
```

    Markup : ```javascript
             ```

* Bullet list
    * Nested bullet
        * Sub-nested bullet etc
* Bullet list item 2

~~~
 Markup : * Bullet list
              * Nested bullet
                  * Sub-nested bullet etc
          * Bullet list item 2
~~~

1. A numbered list
    1. A nested numbered list
    2. Which is numbered
2. Which is numbered

~~~
 Markup : 1. A numbered list
              1. A nested numbered list
              2. Which is numbered
          2. Which is numbered
~~~

- [ ] An uncompleted task
- [x] A completed task

~~~
 Markup : - [ ] An uncompleted task
          - [x] A completed task
~~~

> Blockquote
>> Nested blockquote

    Markup :  > Blockquote
              >> Nested Blockquote

_Horizontal line :_
- - - -

    Markup :  - - - -

_Image with alt :_

![picture alt](http://www.brightlightpictures.com/assets/images/portfolio/thethaw_header.jpg "Title is optional")

    Markup : ![picture alt](http://www.brightlightpictures.com/assets/images/portfolio/thethaw_header.jpg "Title is optional")

Foldable text:

<details>
  <summary>Title 1</summary>
  <p>Content 1 Content 1 Content 1 Content 1 Content 1</p>
</details>
<details>
  <summary>Title 2</summary>
  <p>Content 2 Content 2 Content 2 Content 2 Content 2</p>
</details>

    Markup : <details>
               <summary>Title 1</summary>
               <p>Content 1 Content 1 Content 1 Content 1 Content 1</p>
             </details>

```html
<h3>HTML</h3>
<p> Some HTML code here </p>
```

Hotkey:

<kbd>⌘F</kbd>

<kbd>⇧⌘F</kbd>

    Markup : <kbd>⌘F</kbd>

Hotkey list:

| Key | Symbol |
| --- | --- |
| Option | ⌥ |
| Control | ⌃ |
| Command | ⌘ |
| Shift | ⇧ |
| Caps Lock | ⇪ |
| Tab | ⇥ |
| Esc | ⎋ |
| Power | ⌽ |
| Return | ↩ |
| Delete | ⌫ |
| Up | ↑ |
| Down | ↓ |
| Left | ← |
| Right | → |

Emoji:

:exclamation: Use emoji icons to enhance text. :+1:  Look up emoji codes at [emoji-cheat-sheet.com](http://emoji-cheat-sheet.com/)

    Markup : Code appears between colons :EMOJICODE:

