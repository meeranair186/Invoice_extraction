# Invoice Extractor Model

This project extracts key details from invoice images such as:
- Total Value
- Number of Items
- Bill Date
- And more...

## Prerequisites
Before you can use the model, make sure you have the following installed:
- Python 3.6+
- Pip (for installing dependencies)

## Setup

1. **Clone the repository**  
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/invoice-extractor.git
   cd invoice-extractor
   ```

2. **Install dependencies**  
   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key**  
   Create a `.env` file in the project root directory and add your API key:
   ```bash
   API_KEY=your-api-key-here
   ```

4. **Run the model**  
   You can now run the model with your input image:
   ```bash
   python run_extractor.py --image path/to/invoice.jpg
   ```

## Screenshots

Here's a screenshot of the model in action:
<img width="938" alt="image" src="https://github.com/user-attachments/assets/232edf8a-5d7e-4324-a592-eba2e4209af9">
<img width="388" alt="image" src="https://github.com/user-attachments/assets/cdc4173f-397d-4a70-9ef2-b2123e50089c">




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can replace the path for the screenshot and adjust the filenames as necessary. Also, remember to replace `your-api-key-here` with a placeholder for the actual key format.
