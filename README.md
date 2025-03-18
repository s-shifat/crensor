# Crensor


This is a data handling library built in top of [`pandas`](https://pandas.pydata.org/) and friends

It is specifically designed to work on a specific timesieries sensor data collected in [CREATELAB](https://sites.google.com/d/1GwwjRK1G4GCpFvB04ilbo9HEXWuIQQly/p/1E5hh4221vxXGa8FiUDTapCxAzJilCPJv/edit?pli=1) experiments.


## Installation

There are manyways to install the library.

### Using `pip`
I would recommend to maintain a virtual environment. Although not mandatory.

* Navigate to your proeject directory and create a virtual environment:

    ```bash
    cd path/to/your/project
    python -m venv venv
    ```

* Install the library

    ```bash
     pip install git+https://github.com/s-shifat/crensor.git --upgrade
    ```

It will install everything including jupyter notebook. So you can launch jupyter notebook by:

```bash
jupyter notebook .
```

---

More faster and robust way is to use `uv`:


### Using [`uv`](https://docs.astral.sh/uv/) (**Recommended**)


>If `uv` is not installed, it can easily be installed using one of the following commands.
The installation should be few seconds. It is only a one time process. More on [official website](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)

>##### Windows
>Open powershell and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

>##### Linux and macOS
>Open terminal and run:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

To install `crensor` you can initiate a `uv` project and simply add the library.
All dependencies will be installed automatically.

1. Initialize a project

    ```bash
    uv init yourproject
    ```

2. Add the library

    ```bash
    uv add https://github.com/s-shifat/crensor.git
    ```
2. Activate virtual environment

    **Windows**
    ```powershell
   .\.venv\Scripts\activate.ps1 
    ```

    **Linux/macOS**
    ```bash
   source .venv/bin/activate
    ```

1. Now Launch a jupyter notebook and start coding
    ```bash
   jupyter notebook .
    ```

     Or, If you rather wrote a script, then to execute it run:
    ```bash
   uv run yourscript.py 
    ```



## Updating

As this library is under development. A update may be required.

If using pip:

```bash
 pip install git+https://github.com/s-shifat/crensor.git --upgrade
```


If using uv:
```bash
uv sync
```







