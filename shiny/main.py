import os
from analysis.utils.util import download_files
from analysis.dialogue import wordcloud
from lumos import app


def main():
    try:
        print("Downloading files...")
        download_files()  # Attempt to download files from S3
        print('Files downloaded successfully. Preparing Lumos Server...')

        # Check if all required files exist before starting the application
        required_files = ['characters.csv', 'dialogue.csv', 'places.csv', 'spells.csv']
        all_files_exist = all(os.path.exists(os.path.join('data', f)) for f in required_files)

        if all_files_exist:
            print('All files found...')
            wordcloud()

            # Return the Shiny application to be picked up by shiny run
            return app
        else:
            raise FileNotFoundError("One or more required files are missing after download.")

    except Exception as e:
        print(f'Failed: {e}')
        return None


# Ensure the app is returned properly for shiny run to pick it up
app = main()
