# Step 1: Setup Python

## Install Python

## Setup a virtual environment (optional)
```
python -m venv openai-env
```

Once you’ve created the virtual environment, you need to activate it. On Windows, run:
```
openai-env\Scripts\activate
```

On Unix or MacOS, run:
```
source openai-env/bin/activate
```

Install the OpenAI Python library
```
pip install --upgrade openai
```

## Install the OpenAI Python library

From the terminal / command line, run:
```
pip install --upgrade openai
```

<br />
<br />

# Step 2: Setup your API key

## Setup your API key for all projects (recommended)

### MacOS
```
export OPENAI_API_KEY='your-api-key-here'
```

### Windows

```
setx OPENAI_API_KEY "your-api-key-here"
```