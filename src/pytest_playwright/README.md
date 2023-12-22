# Pytest

## Run the tests

Go to the test folder and execute the command:

```bash
pytest
```

If you want to see the browser excetution, use the flag --headed, for example:

```bash
pytest --headed src/playwright/py_test_with_playwriht.py
```

Execute the tests with a base url and specific browser, allow to have only the relative path in the test, for example:

```bash
pytest --headed src/playwright/py_test_with_playwriht.py --base-url=https://www.google.com --browser=chromium
```

Execute the test saving the traces for analyze the performance, for example:

```bash
pytest --headed src/playwright/py_test_with_playwriht.py --base-url=https://www.google.com --browser=chromium --tracing on
```

# Playwright

## Some commands

Analisys the traces with the command:

```bash
playwright show-trace test-results/src-playwright-py-test-with-playwriht-py-test-sauce-demo-inventory-site-chromium/trace.zip
```

Use codegen to generate the code for the test, for example:

```bash
playwright codegen https://www.google.com
```

Emulate devices 

```bash
--device="Pixel 7"   
```

Emulates geolocation, language and timezone

```bash
--geolocation="51.501,-0.125" --lang=fr-CH --timezone="Europe/Rome"
```

Debugging

Add page.pause() in the test and run the test with the flag --headed, for example:

```bash
pytest --headed src/playwright/py_test_with_playwriht.py
```

https://playwright.dev/docs/debug