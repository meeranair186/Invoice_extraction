# Invoice_extraction
Invoice Extractor Model
This project extracts key details from invoice images such as:

Total Value
Number of Items
Bill Date
And more...
Prerequisites
Before you can use the model, make sure you have the following installed:

Python 3.6+
Pip (for installing dependencies)
Setup
Clone the repository
Clone the repository to your local machine:

git clone https://github.com/your-username/invoice-extractor.git
cd invoice-extractor
Install dependencies
Install the required Python packages using pip:

pip install -r requirements.txt
Configure your API key
Create a .env file in the project root directory and add your API key:

API_KEY=your-api-key-here
Run the model
You can now run the model with your input image:

python run_extractor.py --image path/to/invoice.jpg
