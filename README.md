# Active Desktop

A simple program that keeps your desktop active by slowly moving your mouse in a circle.

## Installation

Clone the repository, then install the dependencies globally or with a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

See options with the `--help` flag:

```bash
python main.py --help
```

### Typical options:

```bash
python main.py --sleep 1 --duration 3
```

Sleep time is specified in seconds and represents the time between each mouse movement.
Duration is specified in hours and represents the maximum time the program will run for.

### Customizing mouse movement:

You can also customize the dimensions of the circle that your mouse will move in:

```bash
python main.py --radius 10 --step 10
```

This will move the mouse in a circle with a radius of 10 units and a step size of 10 degrees.
