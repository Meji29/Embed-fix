import re
import os

def fixup_links(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read()
    print("Content read from input file (fixup_links):", content)  # Debug print

    # Regex to find x.com links
    pattern = re.compile(r'https://x\.com/(\w+/status/\d+)')
    matches = pattern.findall(content)
    print("Matches found for x.com links:", matches)  # Debug print

    with open(output_file_path, 'w') as file:  # Use 'w' to write to the file
        for i, match in enumerate(matches):
            fixed_link = f'https://fixupx.com/{match}'
            file.write(fixed_link + '\n')
            if (i + 1) % 5 == 0:
                file.write('--------------\n')

def fixup_bsky_links(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read()
    print("Content read from input file (fixup_bsky_links):", content)  # Debug print

    # Regex to find bsky.app links
    pattern = re.compile(r'https://bsky\.app/profile/(\w+\.\w+)/post/(\w+)')
    matches = pattern.findall(content)
    print("Matches found for bsky.app links:", matches)  # Debug print

    with open(output_file_path, 'a') as file:  # Use 'a' to append to the file
        for i, match in enumerate(matches):
            fixed_link = f'https://fxbsky.app/profile/{match[0]}/post/{match[1]}'
            file.write(fixed_link + '\n')
            if (i + 1) % 5 == 0:
                file.write('--------------\n')

if __name__ == "__main__":
    # Use the current working directory
    current_dir = os.getcwd()
    
    input_file_path = os.path.join(current_dir, 'input.txt')  # Input file path
    output_file_path = os.path.join(current_dir, 'output.txt')  # Output file path
    
    # Create a sample input.txt if it doesn't exist
    if not os.path.exists(input_file_path):
        with open(input_file_path, 'w') as file:
            file.write('\n')
    
    fixup_links(input_file_path, output_file_path)
    fixup_bsky_links(input_file_path, output_file_path)