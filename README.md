# EMAIL SORTER

Our group has been given a task to create an email sorter. Emails are represented as .txt files, but you can also get
some another file format as input, and your final task is to sort them however you think is correct.

So we decided to split all email in 7 groups
- Spam
- Failures and incidents
- Access requests
- Human resources
- Documents and notifications
- Not an email
- Unknown category

To identify an email from first five groups we can search for special keywords, list of which you can see in config.yaml
file, you can always change the config by adding your own categories and keywords. To find keywords regular expressions 
were used. Files with format different from .txt go to **Not an email** folder. And files without any key word are being 
moved to **Unknown category**.

The sorter has an input and output folders, each of one can be specified in config. To sort files, move them to input folder.
The files would be sorted into different folders in the output folder. You can choose to run your script once ot keep it
running to sort your emails in real time.

To check an email for keyword, regular expressions for each category are being used. Each keyword has its own weight. The more total sum of
found keywords, the more likely the email belongs to this category. If an email has same total sum in two different categories,
the category is being identified by amount of word met. If the sum stays the same, the lower your amount of words, the higher
score per found word, the more likely it is the right category.

An additional logging is being provided. The info about moving files and errors are being written to the logs. It the logs
are enabled. You can specify logs' level and file in configuration. The logs are being written to the console and the file at
the same time.

Total statistic is shown at the end. You can see total amount of files proceeded and amount of emails in each category.

# Downloading and running the script

### 1. Download script

```bash
git clone https://github.com/middelmatigheid/email-sorter.git
cd email-sorter
```

### 2. Specify config

Open config.yaml and specify your config as the template below

```bash
input_folder: YOUR_INPUT_FOLDER           # Folder where your inbox goes
output_folder: YOUR_OUTPUT_FOLDER         # Folder where you want to see your emails sorted

logs_level: YOUR_LOGS_LEVEL_HERE          # Can be "info" or "error"
logs_file: YOUR_LOGS_FILE                 # File for writing logs, should have .txt extension

categories:
  - YOUR_CATEGORY:                        # Do not use / in name of your category
    - word: YOUR_WORD                     # Can be any word or regular expression
      weight: YOUR_WORD_WEIGHT            # Should be an integer
    - word: YOUR_SECOND_WORD              # You can have as much words as you want
      weight: YOUR_SECOND_WORD_WEIGHT     # Make sure to always specify words weight
      
  - YOUR_SECOND_CATEGORY:                 # You can have as much categories as you want
    - word: YOUR_WORD               
      weight: YOUR_WORD_WEIGHT     
    - word: YOUR_SECOND_WORD               
      weight: YOUR_SECOND_WORD_WEIGHT     
```

### 3. Download requirements

```bash
pip install -r requirements.txt
```

### 4. Run the script

Run the command below

```bash
python src/main.py
```

You can add flag **--loop** for keep running the script until stopped for sorting your email in real time

```bash
python src/main.py --loop
```

You can add flag **--logs** for writing the logs

```bash
python src/main.py --logs
```

Or you can add both

```bash
python src/main.py --loop --logs
```

### 5. Run tests

Run the command below for running the tests

```bash
pytest
```

# Project structure

```bash
email-sorter/
├── main.py                     # Main server to run
├── internal/                 
│   ├── config/config.py        # Reading config from .yaml to Config class
│   ├── handler/                # Handling files
│   │   ├── base_handler.py     
│   │   └── handler.py       
│   ├── logger/                 # Logging messages
│   │   ├── base_logger.py
│   │   └── logger.py  
│   ├── metrics/                # Providing metrics
│   │   ├── base_metrics.py 
│   │   └── metrics.py  
│   ├── models/                 # Main models
│   │   ├── category.py
│   │   ├── config.py
│   │   └── word.py  
│   ├── regexp/                 # Getting texts' match value
│   │   ├── base_regexp.py
│   │   └── regexp.py  
│   └── service/                # Getting texts' category
│       ├── base_service.py
│       └── service.py  
├── test/internal/              # Testing main logic
│   ├── handler_test.py
│   ├── metrics_test.py
│   ├── regexp_test.py
│   └── service_test.py
├── config.yaml                 # Config
└── pytest.ini                  # Config for pytest
```

# Authors

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://github.com/middelmatigheid.png" width="100" style="border-radius: 50%;">
        <a href="https://github.com/middelmatigheid" style="display:block;">middelmatigheid</a>
      </td>
      <td align="center">
        <img src="https://github.com/Vadimka217.png" width="100" style="border-radius: 50%;">
        <a href="https://github.com/Vadimka217" style="display:block;">Vadimka217</a>
      </td>
      <td align="center">
        <img src="https://github.com/Dbmda.png" width="100" style="border-radius: 50%;">
        <a href="https://github.com/Dbmda" style="display:block;">Dbmda</a>
      </td>
      <td align="center">
        <img src="https://github.com/mazoxa07.png" width="100" style="border-radius: 50%;">
        <a href="https://github.com/mazoxa07" style="display:block;">mazoxa07</a>
      </td>
      <td align="center">
        <img src="https://github.com/mthw07.png" width="100" style="border-radius: 50%;">
        <a href="https://github.com/mthw07" style="display:block;">mthw07</a>
      </td>
    </tr>
   </table>
</div>
