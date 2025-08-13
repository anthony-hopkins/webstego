# WebStego - Steganography Analysis Toolkit



A web-based steganography analysis tool built with Flask that allows users to analyze JPG and PNG images for hidden messages and embedded files. This toolkit provides a user-friendly interface for digital forensics and security research purposes.

## 🚀 Features

- **Web-Based Interface** - Clean, responsive web UI for easy image analysis
- **Steganography Detection** - Advanced tools to detect hidden data in images
- **Multiple Image Formats** - Support for JPG and PNG image analysis
- **Docker Containerized** - Easy deployment and consistent environment
- **Stego-Toolkit Integration** - Built on top of comprehensive steganography tools
- **Real-Time Analysis** - Instant results with detailed output display
- **Professional Styling** - Modern CSS design with responsive layouts

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Git](https://git-scm.com/downloads)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🛠️ Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd webstego
```

### 2. Build and Run with Docker

```bash
# Build the Docker image
docker build -t webstego .

# Run the container
docker run -d -p 5000:5000 webstego
```

### 3. Access the Application

Open your web browser and navigate to:
- **WebStego Toolkit**: http://localhost:5000

### 4. Alternative: Use the Build Script

For quick rebuilding and deployment:

```bash
chmod +x build.sh
./build.sh
```

## 🏗️ Project Structure

```
webstego/
├── main.py                    # Flask application entry point
├── Dockerfile                 # Container definition
├── build.sh                   # Quick rebuild script
├── templates/                 # HTML templates
│   ├── index.html            # Main upload interface
│   └── runstego.html         # Analysis results page
└── static/                    # CSS stylesheets
    ├── baseline.css          # Main page styling
    └── runstego.css          # Results page styling
```

## 🔧 Configuration

### Docker Configuration

The application runs in a container based on the `ahop1983/stego-toolkit-updated:latest` image, which includes:

- **Steganography Tools** - Comprehensive toolkit for image analysis
- **Python Environment** - Flask runtime and dependencies
- **System Dependencies** - Required libraries and utilities

### Environment Variables

- `LC_ALL=C.UTF-8` - Locale configuration
- `LANG=C.UTF-8` - Language settings

## 📦 Dependencies

### Core Components

- **Flask** - Web framework for the application
- **Stego-Toolkit** - Advanced steganography analysis tools
- **Python** - Runtime environment
- **Docker** - Containerization platform

### System Requirements

- **Base Image**: `ahop1983/stego-toolkit-updated:latest`
- **Port**: 5000 (configurable)
- **Memory**: Minimum 512MB recommended
- **Storage**: Minimal disk space required

## 🐳 Docker Details

### Container Features

- **Base Image**: Specialized steganography toolkit image
- **Port Exposure**: Web interface on port 5000
- **Volume Mounting**: Templates and static files included
- **Entry Point**: Python application launcher

### Build Process

```bash
# Build image
docker build -t webstego .

# Run container
docker run -d -p 5000:5000 webstego

# View logs
docker logs <container_id>
```

## 🚀 Development Workflow

### Starting Development

```bash
# Start the application
docker-compose up

# Or run directly
docker run -d -p 5000:5000 webstego
```

### Stopping Services

```bash
# Stop container
docker stop <container_id>

# Remove container
docker rm <container_id>

# Clean up images
docker system prune -f
```

### Quick Rebuild

The `build.sh` script provides automated rebuilding:

```bash
./build.sh
```

This script:
1. Stops existing containers
2. Cleans up Docker system
3. Rebuilds the image
4. Runs the new container

## 🔍 Application Features

### Main Interface (`/`)

- **File Upload**: Select JPG or PNG images for analysis
- **Format Validation**: Ensures only supported image types
- **User Guidance**: Clear instructions and descriptions

### Analysis Interface (`/success`)

- **File Confirmation**: Displays selected filename
- **Analysis Trigger**: Button to start steganography analysis
- **Navigation**: Easy return to home page

### Results Display (`/runstego`)

- **Real-Time Output**: Shows analysis results as they process
- **Detailed Information**: Comprehensive steganography findings
- **User-Friendly Format**: Clean, readable output display

## 🚨 Security Notes

- **Research Tool**: Designed for legitimate security research and forensics
- **Educational Purpose**: Intended for learning and analysis
- **No Malicious Use**: Should not be used for harmful purposes
- **File Handling**: Uploaded files are processed securely
- **Container Isolation**: Runs in isolated Docker environment

## 🚀 Production Deployment

For production deployment, consider:

1. **Reverse Proxy**: Use Nginx or Apache for production serving
2. **SSL/TLS**: Enable HTTPS for secure connections
3. **Load Balancing**: Scale across multiple containers
4. **Monitoring**: Add health checks and logging
5. **Backup**: Implement data backup strategies
6. **Authentication**: Add user authentication if needed

## 🔧 Customization

### Adding New Analysis Tools

Extend the steganography capabilities by modifying the analysis commands in `main.py`:

```python
# Example: Add new stego tool
command = os.popen('your_stego_tool /path/to/image')
```

### Styling Modifications

Customize the appearance by editing the CSS files in the `static/` directory:

- `baseline.css` - Main page styling
- `runstego.css` - Results page styling

### Template Customization

Modify the HTML templates in the `templates/` directory to change the user interface and functionality.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Steganography Analysis! 🔍**
