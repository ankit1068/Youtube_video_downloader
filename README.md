# YouTube Video Downloader.

A simple web application built with Python (Flask) and HTML to download YouTube videos by entering their URLs. This project uses `pytubefix` to handle video downloads and provides a clean, user-friendly interface.

## Features-
- Input a YouTube URL via a web form.
- Downloads the video in the highest available resolution (MP4 format).
- Displays success or error messages after the download attempt.
- Lightweight and easy to set up.

## Prerequisites-
- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/youtube-video-downloader.git
   cd youtube-video-downloader
   ```

2. **Install Dependencies**
   Install the required Python packages using pip:
   ```bash
   pip install flask pytubefix
   ```

3. **Project Structure**
   Ensure your folder looks like this:
   ```
   youtube-video-downloader/
   ├── app.py
   ├── templates/
   │   └── index.html
   └── README.md
   ```

## Usage-

1. **Run the Application**
   Start the Flask server:
   ```bash
   python app.py
   ```

2. **Access the Web Interface**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Download a Video**
   - Enter a YouTube video URL (e.g., `https://www.youtube.com/watch?v=dQw4w9WgXcQ`).
   - Click the "Download" button.
   - Check the current directory for the downloaded video file (named after the video title).

## Example Screenshot


## Troubleshooting
- **HTTP Error 403: Forbidden**: If you encounter this error, ensure `pytubefix` is installed (not `pytube`), as it includes fixes for YouTube’s cipher restrictions.
- **Video Not Downloading**: Test with a public, unrestricted video. Age-restricted or private videos may not work due to YouTube limitations.
- **Dependencies**: Run `pip install --upgrade flask pytubefix` to ensure you have the latest versions.

## Limitations
- Downloads are saved to the current directory (custom paths not yet implemented).
- Only supports highest-resolution MP4 downloads (no resolution selection in this version).
- May not work with age-restricted or private videos due to `pytubefix` constraints.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to your fork (`git push origin feature-branch`).
5. Open a Pull Request.

## Legal Notice-
This tool is for educational purposes only. Downloading videos from YouTube may violate its [Terms of Service](https://www.youtube.com/static?template=terms). Ensure you have permission to download any content.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with [Flask](https://flask.palletsprojects.com/) and [pytubefix](https://github.com/JuanBindez/pytubefix).
- Inspired by the need for a simple, web-based video downloader.
  


## Contact 

For any questions or feedback, feel free to contact:

Ankit kumar

Email: your-ankitrajj1068@gmail.com

GitHub: ankit1068
