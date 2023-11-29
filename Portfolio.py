import os
import webbrowser

def open_html_file(file_path):
    webbrowser.open('file://' + file_path, new=2)

if __name__ == "__main__":
    # Replace the following line with the actual path to your HTML file
    html_file_path = os.path.join(os.getcwd(),'MyPortfolio.html')

    open_html_file(html_file_path)
