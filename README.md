# AutomotiveChatbot

---


Building an AI chatbot library or SDK in Python for automobile usage is an exciting and complex project. This kind ofSDK would empower developers to integrate intelligent conversational interfaces directly into vehicle infotainment systems, mobile companion apps, or even diagnostic tools.

The core idea is to create a Python package that can understand user queries related to automobiles, process them, and generate relevant responses or trigger specific actions.

The source code available in this repository will be available for AS IT IS usage.


## Build Status


| Build | Tests | Pages |
|:------|:------|-------|
|       |       |       |



## Folder Structure Conventions

---


Although this layout is pretty straightforward, it has several drawbacks that arise as the app complexity increases.
For example, it will be hard for you to reuse the application logic in other projects because all the functionality is
bundled in ```webapp/__init__.py```. If you split this functionality into modules instead, then you could reuse complete
modules across different projects.



```
/
├── sdk                                     # The Core SDK libary
├── iws                                     # An internal web-service
│    ├── account                            # an account’s rest service.
│    │    ├── v1                            # v1 blueprints/api resources.
│    │    │    ├── routes                   # the routes of api resource.
│    │    │    └──/
│    │    ├── v2                            # v2 blueprints/api resources.
│    │    │    ├── routes                   # the routes of api resource.
│    │    │    └──/
│    │    ├── __init__.py                   # The package initializer
│    │    ├── models.py                     # The model objects
│    │    ├── README.md                     # Instructions and helpful links
│    │    ├── _routes.py
│    │    └──/
│    ├── admin                              # an admin’s rest service.
│    │    ├── __init__.py                   # The package initializer
│    │    └──/
│    ├── api                                # The definition of an external API module.
│    │    ├── __init__.py                   # The package initializer
│    │    └──/
│    ├── common                             # the definition of the common’s models.
│    │    ├── __init__.py                   # The package initializer
│    │    └──/
│    ├── framework                          # the definition of the framework’s models.
│    │    ├── __init__.py                   # The package initializer
│    │    ├── logger                        # The logger module
│    │    └──/
│    ├── resources                          # the definition of the resources’s models.
│    │    ├── __init__.py                   # The package initializer
│    │    └──/
│    ├── rest                               # The definition of the rest api module.
│    │    ├── __init__.py                   # The package initializer
│    │    └──/
│    ├── tests                              # The unit-tests module of an application
│    │    ├── __init__.py                   # The package initializer
│    │    └──/
│    ├── webapp                             # the definition of the webapp’s module.
│    │    ├── static                        # The static contents like css, js etc.
│    │    │    ├── css                      # css files
│    │    │    ├── images                   # image files
│    │    │    ├── js                       # JavaScript files
│    │    ├── templates                     # the application’s templates.
│    │    │    ├── admin                    # the reusable fragments of web views.
│    │    │    ├── fragments                # the reusable fragments of web views.
│    │    │    │    ├── _base.html          # base/parent contents of html files
│    │    │    │    ├── _footer.html        # footer's contents
│    │    │    │    └── _navigation.py      # navigation menu links
│    │    │    └── __init__.py              # The package initializer
│    │    ├── __init__.py                   # The package initializer
│    │    ├── app.py                        # The WSGI web application logic.
│    │    ├── routes.py                     # the definition of the web’s routes.
│    │    └──/
│    ├── __init__.py                        # The package initializer
│    ├── config.py                          # the application configuration parameters.
│    ├── README.md                          # Instructions and helpful links of IWS module
│    └──/
├── README.md                               # Instructions and helpful links
├── robots.txt                              # tells which URLs the search engine crawlers can access on your site
├── AutomotiveChatbot                       # The Automotive Project
└──/
```



# Reference

---



# Author

---

* [Rohtash Lakra](https://github.com/rslakra)



# License

---

This project is licensed under the Apache License - see the [LICENSE.md](https://github.com/rslakra/AiSuite/LICENSE.md)
file for details
