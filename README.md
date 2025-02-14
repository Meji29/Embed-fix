# Fixup Script

This project contains a Python script that processes links from input files and writes the modified links to an output file. It specifically handles links from `x.com` and `bsky.app`.

## Installation

To install this script as a command-line tool, you need to have Python and `pip` installed. Then, follow these steps:

1. Navigate to the project directory:

    ```sh
    cd "C:/Users/meji2/Desktop/Personal Projects/Fixup - Script"
    ```

2. Install the script using `pip`:

    ```sh
    pip install .
    ```

## Usage

Once installed, you can run the script using the command:

```sh
fixup-script
```
The script will read from input.txt and write the modified links to output.txt in the current working directory.

## Script Details
Functions
- fixup_links(input_file_path, output_file_path): Processes x.com links.
- fixup_bsky_links(input_file_path, output_file_path): Processes bsky.app links.

## Main Execution
The script will:

1. Check if input.txt exists in the current working directory. If not, it will create an empty input.txt.

2. Process the links using the fixup_links and fixup_bsky_links functions.

3. Write the modified links to output.txt.

## Example
1. Create an input.txt file in the current directory with some sample links:
```sh
https://x.com/user/status/12345
https://bsky.app/profile/user.domain/post/67890
```
2. Run the script
```sh
fixup-script
```
3. Check the output.txt file for the modified links:
```sh
https://fixupx.com/user/status/12345
--------------
https://fxbsky.app/profile/user.domain/post/67890
--------------
```
