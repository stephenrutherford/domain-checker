# Domain Checker

A fraud analysis tool used to check for invalid and disposable email domains.

![](https://github.com/stephenrutherford/domain-checker/blob/master/banner2.png)

## Features
The app was built in Django using Python where it will perform a web-scrape from the website check-mail.org. The user can paste in the domains that they want to check, and the App will render a results table with two specific columns that contain data of interest.

* Disposable - If the domain is considered disposable.
* Valid - If the domain is able to receive email, or is high risk.

A export button was also included for larger querues. The user may want to download the entire results table as a CSV file for filtering and spreadsheet lookups.

[LIVE DEMO](https://fps-domain-checker.herokuapp.com/)
