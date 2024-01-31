# report_racing_app
***

A Python package for the Formula 1 Monaco Racing Report Generator.

## Installation

Clone the repository to your local machine:

```bash
https://git.foxminded.ua/foxstudent106412/task-6-report-of-monaco-2018-racing.git
```

## How to use the application?
***

The application uses the command-line interface for its operation and supports the following command-line options:
* --files <folder_path>: Specify the folder path containing the log and text files.
* --asc or --desc: Optional. Specify the order for sorting the results (default is asc).
* --driver <abbreviation>: Optional. Show statistics about a specific racer abbreviation.

##### Examples:

To display a list of drivers along with their lap times, use the following command:

    $ python command_interface.py --files <folder_path>

To change the sorting order to descend, use the --desc option:

    $ python command_interface.py --files <folder_path> --desk

To get statistics about a specific driver by their abbreviation, add the --driver option with their abbreviation:

    $ python command_interface.py --files <folder_path> --driver "DRR"

## License
***

[MIT](LICENSE)
