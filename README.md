# Gemini Token Counter

A containerized application that counts tokens for Google Gemini 1.5 Flash model prompts. This app is designed to be deployed on an Azure VM for system health checks and tokenization metrics testing.

## Overview

This application provides token counting functionality for the Google Gemini API. It validates your Gemini API key, executes token counting operations, and outputs metrics for monitoring purposes.

## Prerequisites

- Docker and Docker Compose installed on your Azure VM
- Google Gemini API key (get one at [Google AI Studio](https://aistudio.google.com/))
- Python 3.9+ (for local development)

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd gemini_devops_deploy
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Gemini API key.

**Important:** Never commit the `.env` file to version control.

### 3. Local Development

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Docker Deployment

### Build and Run with Docker Compose

```bash
docker-compose up --build
```

This will:
1. Build the Docker image from the Dockerfile
2. Create a container named `gemini_counter`
3. Load the `.env` file for environment variables
4. Execute the token counting test

### View Output

After running, you should see output similar to:

```
--- CONTAINER OUTPUT ---
Target: Gemini 1.5 Flash
Payload Tokens: XX
--- END OUTPUT ---
```

## Azure VM Deployment

### 1. Prepare the Azure VM

- Create an Ubuntu 20.04 LTS VM on Azure
- SSH into the VM
- Install Docker and Docker Compose:

```bash
sudo apt-get update
sudo apt-get install -y docker.io docker-compose
sudo usermod -aG docker $USER
```

### 2. Deploy the Application

Clone the repository and configure the environment:

```bash
git clone <repository-url>
cd gemini_devops_deploy
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### 3. Run the Container

```bash
docker-compose up
```

Or run in detached mode to run as a background task:

```bash
docker-compose up -d
```

View logs:

```bash
docker-compose logs gemini_counter
```

## Project Structure

```
gemini_devops_deploy/
├── main.py                # Main application code
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container configuration
├── docker-compose.yml    # Docker Compose orchestration
├── .env                  # Environment variables (not in repo)
└── README.md            # This file
```

## Application Details

### `main.py`

The core application that:
- Loads the Gemini API key from environment variables
- Initializes the Google Generative AI client
- Counts tokens for a test prompt using Gemini 1.5 Flash
- Handles errors gracefully with error codes

**Key Function:**
- `get_token_count(prompt_text)`: Returns the token count for a given prompt. Returns `-1` on error.

### Dependencies

| Package | Purpose |
|---------|---------|
| `google-generativeai` | Google Gemini API client library |
| `python-dotenv` | Load environment variables from `.env` file |

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Your Google Gemini API key | Yes |

## Troubleshooting

### "GEMINI_API_KEY var not loaded"

**Issue:** The application exits immediately with this message.

**Solution:** Ensure the `.env` file exists in the root directory and contains `GEMINI_API_KEY=your_key_here`.

### Container fails to build

**Issue:** Docker build fails with dependency errors.

**Solution:** Ensure `requirements.txt` is in the root directory and contains the required packages.

### API authentication error

**Issue:** "Error authenticating with Google API"

**Solution:** Verify your Gemini API key is valid and active in Google AI Studio.

## License

This project is proprietary.

## Support

For issues or questions, contact your DevOps team.
