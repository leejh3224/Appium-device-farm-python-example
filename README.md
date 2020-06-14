# Appium Device Farm Python Example

This repository gives you a simple python example of using Appium and Device Farm together for testing web apps.

I found out that `web app` sample in [official example on aws-samples](https://github.com/aws-samples/aws-device-farm-appium-python-tests-for-android-sample-app) just simply doesn't work.

So I did a bit of a research, and finally made it work.

It seems like AWS sample project is targeting `Python 2`.

In order to use `Python 3`, You need to select `custom text environment`.

And also when you're making a zip file, generating `wheelhouse` archive is no longer required.

It's mentioned in [aws documentation](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-appium.html)

## Getting Started

Make sure you have `Python 3` and `node.js` installed first.

Then activate `virtualenv` and install dependencies.

```bash
cd appium-device-farm-example

# create virtualenv
python3 -m venv venv

# active virtualenv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# you also need to install appium
npm install -g appium

# run appium server
# use another terminal for this
appium

# use local environment capabilities -> checkout `setUp` method of test file
# run test
python3 -m unittest
```

## Deploy

Run `build.sh` and upload `test_bundle.zip` file in aws device farm web console following instructions [here](https://docs.aws.amazon.com/devicefarm/latest/developerguide/getting-started.html).

```bash
# make it executable
chmod +x build.sh

# generate zip file
./build.sh
```

Make sure you have selected `custom environment` and changed python version to 3.

```yaml
phases:
  install:
    commands:
      - export PYTHON_VERSION=3
      # ...
      - export APPIUM_VERSION=1.14.2
      # ...
```

## Trouble Shotting

### Wheel files are alwayes generated with platforms other than 'linux-x86-64'

> You no longer need to generate wheelfiles if you're targeting Python 3.

Wheel files are platform specific. So you need to make it `universal` (none-any).

There are several ways to do this but the fastest way is to create `setup.cfg` file in your project's root directory.

```cfg
[bdist_wheel]
universal = 1
```

If you still have platform specific wheel files then simiply renaming it to `none-any` will work.

### Appium not waiting for keypress

You can checkout `wait_for_input_text` function inside `tests/test_example.py`.

It uses selenium's explicit wait (`WebDriverWait`) to wait until a text field has specific text value.

### Test runs are always empty! (Ran 0 tests in 0.000s)

In python, name of every test case should start with `test` otherwise `unittest` will skip that.

Make sure you have named your test cases following the convention.
