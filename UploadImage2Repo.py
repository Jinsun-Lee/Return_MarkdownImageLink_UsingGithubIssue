import os
from github import Github

# TODO
REPO_NAME = 'your_repository_name'
GITHUB_TOKEN = 'your_github_token'
    
"""
이미지가 지정한 레포지토리로 업로드는 되는데
이슈에 올라간 것도 아니고
이미지 링크도 가짜임
"""

def upload_image_to_github(file_path, repo_name, github_token):
    
    # Connect to GitHub
    g = Github(github_token)
    repo = g.get_user().get_repo(repo_name)

    # Upload image to GitHub
    with open(file_path, 'rb') as file:
        content = file.read()
        filename = os.path.basename(file_path)

        result = repo.create_file(filename, f"Upload {filename}", content)
        image_url = result["content"].download_url if "content" in result else None

    return image_url

def print_image_files(current_path):
    print("\n")
    files_in_directory = os.listdir(current_path)
    for file_name in files_in_directory:
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(file_name)
    print("\n")

    
def main():
    # check current path image files name
    current_path = os.getcwd()
    print_image_files(current_path)
    
    # enter image file
    image_name = input("Enter the image name: ")
    image_path = os.path.join(current_path, image_name)

    # check if the file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_name}' not found.")
        return

    # gitHub repository information
    repo_name = REPO_NAME
    github_token = GITHUB_TOKEN

    # upload image to gitHub and get the image URL
    image_url = upload_image_to_github(image_path, repo_name, github_token)

    # print the image URL
    print(f"Image uploaded successfully.\n\n>>> {image_url}")

if __name__ == "__main__":
    main()