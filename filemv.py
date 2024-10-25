import os
import shutil
import fnmatch

class DesktopCleaner:
    def __init__(self, folder_to_track, ignore_patterns=None):
        self.folder_to_track = folder_to_track
        self.ignore_patterns = ignore_patterns if ignore_patterns else []

    def clean_desktop(self):
        for filename in os.listdir(self.folder_to_track):
            src_path = os.path.join(self.folder_to_track, filename)

            if os.path.isdir(src_path):
                continue

            if any(fnmatch.fnmatch(filename, pattern) for pattern in self.ignore_patterns):
                print(f"Ignoring file: {filename}")
                continue

            self.move_file(src_path)

    def move_file(self, src_path):
        filename = os.path.basename(src_path)

        # file type specification
        if filename.endswith(('.txt', '.sh')):
            dest_folder = os.path.join(self.folder_to_track, 'Text Files')
        elif filename.endswith(('.png', '.jpeg', '.jpg')):
            dest_folder = os.path.join(self.folder_to_track, 'Images')
        elif filename.endswith('.docx'):
            dest_folder = os.path.join(self.folder_to_track, 'Word')
        elif filename.endswith('.pdf'):
            dest_folder = os.path.join(self.folder_to_track, 'PDFs')
        elif filename.endswith(('.csv', '.ods')):
            dest_folder = os.path.join(self.folder_to_track, 'Excel')
        else:
            dest_folder = os.path.join(self.folder_to_track, 'Etc')

        os.makedirs(dest_folder, exist_ok=True)

        new_dest = os.path.join(dest_folder, filename)
        shutil.move(src_path, new_dest)
        print(f"Moved file {filename} to {new_dest}")


# folder_to_track = 'C:/Users/{USER}/Desktop/'
ignore_patterns = ['*.py']  # patterns to ignore

# cleaner object
cleaner = DesktopCleaner(folder_to_track, ignore_patterns)

# method call to clean the desktop
cleaner.clean_desktop()
